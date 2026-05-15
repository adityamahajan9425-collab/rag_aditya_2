"""
AstroRAG — ISRO & NASA Mission Intelligence Chatbot
Streamlit App

Run with: streamlit run app.py
"""

import streamlit as st
import sys
import os

# Allow imports from same directory
sys.path.insert(0, os.path.dirname(__file__))

from rag_engine import get_engine
from llm_client import generate_answer
from knowledge_base import get_all_missions, get_missions_by_agency


# ─── Page Config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AstroRAG | Space Mission Assistant",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────

st.markdown("""
<style>
    /* Dark space theme */
    .stApp {
        background: linear-gradient(135deg, #0a0e1a 0%, #0d1b2a 50%, #0a0e1a 100%);
    }
    
    /* Header */
    .astro-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(90deg, #1a1f3a, #0d1b2a, #1a1f3a);
        border-bottom: 1px solid #00d4ff33;
        margin-bottom: 1.5rem;
        border-radius: 12px;
    }
    .astro-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00d4ff, #7b61ff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200%;
        letter-spacing: 2px;
    }
    .astro-subtitle {
        color: #8899bb;
        font-size: 1rem;
        margin-top: 0.3rem;
    }
    
    /* Chat messages */
    .user-bubble {
        background: linear-gradient(135deg, #1e2d5a, #162040);
        border: 1px solid #3355aa44;
        border-radius: 16px 16px 4px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        color: #cce0ff;
    }
    .bot-bubble {
        background: linear-gradient(135deg, #0d2233, #091a2a);
        border: 1px solid #00d4ff22;
        border-radius: 4px 16px 16px 16px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        color: #ddeeff;
        border-left: 3px solid #00d4ff;
    }
    
    /* Source citations */
    .source-card {
        background: #0d1e30;
        border: 1px solid #00d4ff33;
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        margin: 0.3rem 0;
        font-size: 0.82rem;
        color: #88aacc;
    }
    .source-agency-isro {
        color: #ff7043;
        font-weight: 700;
        font-size: 0.75rem;
    }
    .source-agency-nasa {
        color: #42a5f5;
        font-weight: 700;
        font-size: 0.75rem;
    }
    
    /* Mission cards in sidebar */
    .mission-card {
        background: #0d1e30;
        border-left: 3px solid #00d4ff44;
        padding: 0.5rem 0.7rem;
        margin: 0.4rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.82rem;
        color: #99bbdd;
        cursor: pointer;
    }
    .mission-card:hover {
        border-left-color: #00d4ff;
        background: #122233;
    }
    
    /* Stats badges */
    .badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 600;
        margin: 0.15rem;
    }
    .badge-active { background: #0d3320; color: #4caf50; border: 1px solid #4caf5044; }
    .badge-completed { background: #1a2840; color: #64b5f6; border: 1px solid #64b5f644; }
    .badge-development { background: #2d1f0d; color: #ffa726; border: 1px solid #ffa72644; }
    
    /* Input box */
    .stTextInput > div > div > input {
        background: #0d1e30 !important;
        border: 1px solid #00d4ff44 !important;
        color: #cce0ff !important;
        border-radius: 12px !important;
    }
    
    /* Sidebar */
    .css-1d391kg { background: #070d1a; }
    
    /* Metric boxes */
    .metric-box {
        background: linear-gradient(135deg, #0d1e30, #091525);
        border: 1px solid #00d4ff22;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 0.3rem 0;
    }
    .metric-value { font-size: 1.8rem; font-weight: 800; color: #00d4ff; }
    .metric-label { font-size: 0.75rem; color: #667788; margin-top: 0.2rem; }
    
    /* Suggested questions */
    .suggest-btn {
        background: #0d1e30;
        border: 1px solid #00d4ff33;
        border-radius: 8px;
        padding: 0.5rem 0.8rem;
        color: #88aacc;
        font-size: 0.82rem;
        cursor: pointer;
        margin: 0.2rem 0;
        width: 100%;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)


# ─── Initialise Session State ─────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []          # {"role", "content"}
if "chat_display" not in st.session_state:
    st.session_state.chat_display = []      # {"role", "content", "sources"}
if "engine" not in st.session_state:
    with st.spinner("🛸 Initialising RAG engine and indexing mission knowledge base..."):
        st.session_state.engine = get_engine()
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = bool(os.environ.get("ANTHROPIC_API_KEY"))


# ─── Sidebar ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🛸 AstroRAG")
    st.markdown("*Space Mission Intelligence*")
    st.divider()

    # API Key input
    st.markdown("### 🔑 API Configuration")
    api_key_input = st.text_input(
        "Anthropic API Key",
        type="password",
        value=os.environ.get("ANTHROPIC_API_KEY", ""),
        placeholder="sk-ant-...",
        help="Get your key from console.anthropic.com",
    )
    if api_key_input:
        os.environ["ANTHROPIC_API_KEY"] = api_key_input
        st.session_state.api_key_set = True
        st.success("✅ API key configured")

    st.divider()

    # Agency filter
    st.markdown("### 🔭 Filter by Agency")
    agency_filter = st.radio(
        "Show missions from:",
        options=["All", "ISRO", "NASA"],
        horizontal=True,
    )
    filter_val = None if agency_filter == "All" else agency_filter

    st.divider()

    # Stats
    all_missions = get_all_missions()
    isro_count = len(get_missions_by_agency("ISRO"))
    nasa_count = len(get_missions_by_agency("NASA"))
    active_count = sum(1 for m in all_missions if m["status"] == "Active")
    chunks_count = len(st.session_state.engine.chunks)

    st.markdown("### 📊 Knowledge Base Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{isro_count}</div><div class="metric-label">ISRO Missions</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{nasa_count}</div><div class="metric-label">NASA Missions</div></div>', unsafe_allow_html=True)

    st.markdown(f'<div class="metric-box"><div class="metric-value">{chunks_count}</div><div class="metric-label">Indexed Text Chunks</div></div>', unsafe_allow_html=True)

    st.divider()

    # Mission index
    st.markdown("### 🗂️ Mission Library")
    for mission in all_missions:
        status = mission["status"]
        badge_class = "badge-active" if "Active" in status else ("badge-development" if "Development" in status else "badge-completed")
        agency_color = "#ff7043" if mission["agency"] == "ISRO" else "#42a5f5"

        if filter_val and mission["agency"] != filter_val:
            continue

        st.markdown(
            f'<div class="mission-card">'
            f'<span style="color:{agency_color};font-weight:700;font-size:0.7rem">{mission["agency"]}</span> '
            f'<span class="badge {badge_class}">{status}</span><br>'
            f'<b style="color:#cce0ff">{mission["title"].split("|")[0].strip()}</b><br>'
            f'<span style="color:#556677;font-size:0.7rem">📅 {mission["launch_date"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_display = []
        st.rerun()


# ─── Main Content ─────────────────────────────────────────────────────────────

# Header
st.markdown("""
<div class="astro-header">
    <div class="astro-title">🛸 ASTRORAG</div>
    <div class="astro-subtitle">Retrieval-Augmented Intelligence for ISRO & NASA Space Missions</div>
</div>
""", unsafe_allow_html=True)


# Suggested questions
if not st.session_state.chat_display:
    st.markdown("### 💡 Try asking about:")
    suggestions = [
        "🌙 What did Chandrayaan-3 discover on the Moon?",
        "🔴 How does Mangalyaan compare to NASA's Mars missions?",
        "☀️ What is ISRO's Aditya-L1 mission and its goals?",
        "🔭 What has the James Webb Space Telescope found?",
        "🚀 Tell me about NASA's Artemis program",
        "🤖 What did the Perseverance rover discover on Mars?",
        "⚡ What is the Parker Solar Probe achieving?",
        "🛰️ What records did Voyager spacecraft break?",
    ]

    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(suggestion, key=f"suggest_{i}", use_container_width=True):
                st.session_state._pending_query = suggestion.split(" ", 1)[1]  # remove emoji
                st.rerun()


# ─── Chat History Display ──────────────────────────────────────────────────────

chat_container = st.container()

with chat_container:
    for turn in st.session_state.chat_display:
        if turn["role"] == "user":
            st.markdown(
                f'<div class="user-bubble">🧑‍🚀 <b>You:</b><br>{turn["content"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="bot-bubble">🛸 <b>AstroRAG:</b><br>{turn["content"]}</div>',
                unsafe_allow_html=True,
            )
            # Display citations
            if turn.get("sources"):
                with st.expander(f"📚 {len(turn['sources'])} Source(s) Retrieved", expanded=False):
                    for src in turn["sources"]:
                        agency_class = "source-agency-isro" if src["agency"] == "ISRO" else "source-agency-nasa"
                        st.markdown(
                            f'<div class="source-card">'
                            f'<span class="{agency_class}">{src["agency"]}</span> '
                            f'<b style="color:#cce0ff">{src["label"]} — {src["title"]}</b><br>'
                            f'<span>Relevance Score: <b>{src["relevance_score"]}</b></span><br>'
                            f'<i style="color:#667788">{src["preview"]}</i>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )


# ─── Input Area ───────────────────────────────────────────────────────────────

st.divider()

# Check for pending query from suggestion buttons
initial_query = ""
if hasattr(st.session_state, "_pending_query"):
    initial_query = st.session_state._pending_query
    del st.session_state._pending_query

with st.form("chat_form", clear_on_submit=True):
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_query = st.text_input(
            "Ask about space missions",
            value=initial_query,
            placeholder="e.g. What instruments did Chandrayaan-3 carry?",
            label_visibility="collapsed",
        )
    with col_btn:
        top_k_slider = st.slider("Context chunks", 3, 8, 5, label_visibility="collapsed")
        submitted = st.form_submit_button("🚀 Ask", use_container_width=True)


# ─── Query Processing ─────────────────────────────────────────────────────────

if submitted and user_query.strip():
    query = user_query.strip()

    if not st.session_state.api_key_set:
        st.error("⚠️ Please enter your Anthropic API key in the sidebar first.")
    else:
        # Add user message to display
        st.session_state.chat_display.append({"role": "user", "content": query})

        with st.spinner("🔭 Retrieving relevant mission data..."):
            context, sources = st.session_state.engine.get_context_for_prompt(
                query, top_k=top_k_slider, agency_filter=filter_val
            )

        if not context:
            answer = "I couldn't find relevant information in my knowledge base for that query. Try asking about ISRO or NASA missions like Chandrayaan, Mangalyaan, Artemis, JWST, or Mars rovers."
            sources = []
        else:
            with st.spinner("🤖 Generating answer from context..."):
                result = generate_answer(
                    query=query,
                    context=context,
                    chat_history=st.session_state.messages,
                )

            if result["success"]:
                answer = result["text"]
                # Update message history for multi-turn
                st.session_state.messages.append({"role": "user", "content": query})
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                answer = f"❌ Error from Claude API: {result['error']}"
                sources = []

        st.session_state.chat_display.append({
            "role": "assistant",
            "content": answer,
            "sources": sources,
        })
        st.rerun()


# ─── Footer ───────────────────────────────────────────────────────────────────

st.markdown("""
<hr style="border-color: #00d4ff22; margin-top: 2rem;">
<p style="text-align: center; color: #334455; font-size: 0.75rem;">
AstroRAG · Built for SISTec Gandhi Nagar · RAG Workshop Competition Problem #10<br>
Knowledge base: ISRO (Chandrayaan 1/2/3, Mangalyaan, Aditya-L1, PSLV, Gaganyaan) + NASA (Artemis, JWST, Perseverance, Parker, Voyager)
</p>
""", unsafe_allow_html=True)
