"""
AstroRAG — Command Line Interface Demo
Works without Streamlit; uses Claude API for generation.

Usage:
    python cli_demo.py                          # interactive mode
    python cli_demo.py "What did Chandrayaan-3 discover?"   # single query
    
Environment:
    ANTHROPIC_API_KEY=sk-ant-...  python cli_demo.py
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(__file__))

from rag_engine import get_engine
from llm_client import generate_answer


# ─── ANSI colours ─────────────────────────────────────────────────────────────
CYAN   = "\033[96m"
BLUE   = "\033[94m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"
LINE   = "─" * 70


def banner():
    print(f"\n{CYAN}{BOLD}")
    print("  █████╗ ███████╗████████╗██████╗  ██████╗ ██████╗  █████╗  ██████╗")
    print(" ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝")
    print(" ███████║███████╗   ██║   ██████╔╝██║   ██║██████╔╝███████║██║  ███╗")
    print(" ██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║██╔══██╗██╔══██║██║   ██║")
    print(" ██║  ██║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝")
    print(" ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ")
    print(f"{RESET}")
    print(f"  {BLUE}🛸 Space Mission Intelligence — ISRO & NASA Knowledge Assistant{RESET}")
    print(f"  {DIM}SISTec Gandhi Nagar · RAG Workshop Competition · Problem #10{RESET}")
    print()


def print_sources(sources):
    if not sources:
        return
    print(f"\n{DIM}{'─'*70}{RESET}")
    print(f"{YELLOW}{BOLD}📚 Retrieved Sources:{RESET}")
    for src in sources:
        agency_color = "\033[91m" if src["agency"] == "ISRO" else "\033[94m"
        print(
            f"  {src['label']} {agency_color}{BOLD}{src['agency']}{RESET} — "
            f"{src['title']}"
        )
        print(f"      {DIM}Relevance: {src['relevance_score']} | {src['preview'][:120]}...{RESET}")


def run_query(engine, query: str, chat_history: list, agency_filter: str = None, top_k: int = 5):
    print(f"\n{CYAN}🔭 Retrieving relevant mission chunks...{RESET}")
    t0 = time.time()
    context, sources = engine.get_context_for_prompt(query, top_k=top_k, agency_filter=agency_filter)
    retrieval_time = time.time() - t0

    if not context:
        print(f"{RED}No relevant documents found for that query.{RESET}")
        return None, []

    print(f"{GREEN}✓ Found {len(sources)} relevant mission(s) in {retrieval_time:.3f}s{RESET}")
    print_sources(sources)

    has_key = bool(os.environ.get("ANTHROPIC_API_KEY"))
    if not has_key:
        print(f"\n{YELLOW}⚠️  ANTHROPIC_API_KEY not set — showing raw context only{RESET}")
        print(f"\n{DIM}{'─'*70}{RESET}")
        print(f"{BOLD}📄 Retrieved Context:{RESET}\n")
        print(context[:1500] + "...")
        return None, sources

    print(f"\n{CYAN}🤖 Generating answer with Claude...{RESET}")
    t1 = time.time()
    result = generate_answer(query, context, chat_history)
    gen_time = time.time() - t1

    if result["success"]:
        print(f"{GREEN}✓ Answer generated in {gen_time:.2f}s{RESET}\n")
        print(f"{DIM}{'─'*70}{RESET}")
        print(f"{BOLD}{BLUE}🛸 AstroRAG:{RESET}\n")
        print(result["text"])
        return result["text"], sources
    else:
        print(f"{RED}API Error: {result['error']}{RESET}")
        return None, sources


def interactive_mode(engine):
    banner()
    print(f"{BLUE}{LINE}{RESET}")
    print(f"Type your space mission question below.")
    print(f"Commands: {BOLD}quit{RESET} | {BOLD}clear{RESET} | {BOLD}filter isro{RESET} | {BOLD}filter nasa{RESET} | {BOLD}filter all{RESET}")
    print(f"{BLUE}{LINE}{RESET}\n")

    chat_history = []
    agency_filter = None
    filter_display = "All Agencies"

    while True:
        try:
            prompt = f"{YELLOW}[{filter_display}] >{RESET} "
            query = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{DIM}Goodbye! Safe travels through the cosmos. 🚀{RESET}\n")
            break

        if not query:
            continue

        # Commands
        if query.lower() in ("quit", "exit", "q"):
            print(f"{DIM}Goodbye! 🚀{RESET}\n")
            break
        elif query.lower() == "clear":
            chat_history.clear()
            print(f"{GREEN}✓ Conversation cleared.{RESET}")
            continue
        elif query.lower() == "filter isro":
            agency_filter = "ISRO"
            filter_display = "ISRO Only"
            print(f"{GREEN}✓ Filtering to ISRO missions.{RESET}")
            continue
        elif query.lower() == "filter nasa":
            agency_filter = "NASA"
            filter_display = "NASA Only"
            print(f"{GREEN}✓ Filtering to NASA missions.{RESET}")
            continue
        elif query.lower() in ("filter all", "filter none"):
            agency_filter = None
            filter_display = "All Agencies"
            print(f"{GREEN}✓ Showing all missions.{RESET}")
            continue

        print(f"\n{BOLD}You:{RESET} {query}")
        answer, sources = run_query(engine, query, chat_history, agency_filter)

        if answer:
            chat_history.append({"role": "user", "content": query})
            chat_history.append({"role": "assistant", "content": answer})
            # Keep last 6 turns
            if len(chat_history) > 12:
                chat_history = chat_history[-12:]

        print(f"\n{BLUE}{LINE}{RESET}")


def demo_mode(engine):
    """Run preset demo questions to showcase the RAG system."""
    banner()
    print(f"{BOLD}Running DEMO MODE — preset questions{RESET}\n")

    demo_questions = [
        ("ISRO", "What did Chandrayaan-3 discover on the lunar south pole?"),
        ("NASA", "What are the main achievements of the Perseverance rover?"),
        (None, "Compare ISRO's Mangalyaan and NASA's Mars missions"),
        (None, "What is the James Webb Space Telescope's most important discovery?"),
        ("ISRO", "Explain the Aditya-L1 mission and its scientific instruments"),
    ]

    chat_history = []

    for filter_agency, question in demo_questions:
        print(f"\n{BLUE}{'═'*70}{RESET}")
        print(f"{BOLD}QUESTION:{RESET} {question}")
        if filter_agency:
            print(f"{DIM}Filter: {filter_agency} only{RESET}")
        print(f"{BLUE}{'═'*70}{RESET}")

        answer, sources = run_query(engine, question, chat_history, filter_agency)
        if answer:
            chat_history.append({"role": "user", "content": question})
            chat_history.append({"role": "assistant", "content": answer})

        print("\n")
        time.sleep(0.5)


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"{CYAN}Loading RAG engine...{RESET}")
    engine = get_engine()

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        if query == "--demo":
            demo_mode(engine)
        else:
            banner()
            print(f"{BOLD}Query:{RESET} {query}\n")
            run_query(engine, query, [], top_k=5)
    else:
        interactive_mode(engine)
