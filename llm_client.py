"""
LLM Client — calls Google Gemini API to generate answers from RAG context
Uses: gemini-2.0-flash via generateContent REST endpoint (no SDK required)
"""

import os
import json
import urllib.request
import urllib.error


SYSTEM_PROMPT = """You are **AstroRAG** — an expert AI assistant specialised in ISRO and NASA space missions.

You answer questions using ONLY the provided context (retrieved mission documents). 
Your answers must:
1. Be accurate, well-structured, and cite sources using [Source N] markers from the context
2. Explain mission objectives, instruments, outcomes, timelines, and scientific significance
3. Distinguish between ISRO and NASA missions clearly when relevant
4. When asked about comparisons, provide balanced scientific perspectives
5. If information is not in the context, say "I don't have data on that in my knowledge base" — do NOT hallucinate
6. Use appropriate scientific terminology while remaining accessible
7. Include dates, measurements, and specific details when available in context

Format your answers clearly. Use bullet points for lists of instruments/objectives.
Use bold for mission names and key findings. Always end with the cited sources."""


GEMINI_MODEL    = "gemini-2.0-flash"
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def build_rag_prompt(query: str, context: str) -> str:
    return f"""Here are the relevant space mission documents retrieved for this query:

--- BEGIN CONTEXT ---
{context}
--- END CONTEXT ---

User Question: {query}

Please answer the question using the context above. Cite sources as [Source N] inline."""


def _build_contents(chat_history: list[dict], query: str, context: str) -> list[dict]:
    """
    Build Gemini-format 'contents' array.
    Gemini roles are 'user' / 'model' (not 'assistant').
    Prior history is included for multi-turn memory.
    The final turn contains the RAG-augmented prompt.
    """
    contents = []

    for msg in chat_history:
        role = "user" if msg["role"] == "user" else "model"
        contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}],
        })

    # Final RAG-augmented user turn
    contents.append({
        "role": "user",
        "parts": [{"text": build_rag_prompt(query, context)}],
    })

    return contents


def call_gemini_api(chat_history: list[dict], query: str, context: str,
                    system: str = SYSTEM_PROMPT) -> dict:
    """
    POST to Gemini generateContent endpoint.
    Returns {"success": bool, "text": str, "error": str}
    """
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return {
            "success": False,
            "text": "",
            "error": (
                "GEMINI_API_KEY not set.\n"
                "Get a free key at: https://aistudio.google.com/apikey\n"
                "Then set it in the sidebar or run:  export GEMINI_API_KEY=your_key"
            ),
        }

    payload = {
        "system_instruction": {
            "parts": [{"text": system}]
        },
        "contents": _build_contents(chat_history, query, context),
        "generationConfig": {
            "maxOutputTokens": 1024,
            "temperature": 0.2,
        },
    }

    url  = f"{GEMINI_API_BASE}/{GEMINI_MODEL}:generateContent?key={api_key}"
    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            # Gemini response: result["candidates"][0]["content"]["parts"][0]["text"]
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"success": True, "text": text, "error": ""}

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            msg = json.loads(body).get("error", {}).get("message", body)
        except Exception:
            msg = body
        return {"success": False, "text": "", "error": f"HTTP {e.code}: {msg}"}

    except Exception as e:
        return {"success": False, "text": "", "error": str(e)}


def generate_answer(query: str, context: str, chat_history: list[dict] = None) -> dict:
    """
    Public entry point used by app.py and cli_demo.py.
    chat_history: [{"role": "user"/"assistant", "content": str}, ...]
    """
    history = (chat_history or [])[-6:]   # keep last 6 turns
    return call_gemini_api(history, query, context)
