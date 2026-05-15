"""
LLM Client — calls Google Gemini API to generate answers from RAG context
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
Use bold for mission names and key findings. Always end with the cited sources.
"""


def build_rag_prompt(query: str, context: str) -> str:
    return f"""Here are the relevant space mission documents retrieved for this query:

--- BEGIN CONTEXT ---
{context}
--- END CONTEXT ---

User Question: {query}

Please answer the question using the context above. Cite sources as [Source N] inline.
"""


def call_gemini_api(messages: list[dict], system: str = SYSTEM_PROMPT) -> dict:
    """
    Call the Google Gemini REST API.
    Returns {"success": bool, "text": str, "error": str}
    """
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return {
            "success": False,
            "text": "",
            "error": "GEMINI_API_KEY not set. Please set it in your environment variables.",
        }

    # Convert messages from OpenAI/Claude format to Gemini format
    # Gemini uses "user" and "model" roles, with "parts" instead of "content"
    gemini_contents = []
    for msg in messages:
        role = msg["role"]
        if role == "assistant":
            role = "model"  # Gemini uses "model" instead of "assistant"
        gemini_contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}],
        })

    payload = {
        "contents": gemini_contents,
        "systemInstruction": {
            "parts": [{"text": system}],
        },
        "generationConfig": {
            "maxOutputTokens": 1024,
            "temperature": 0.7,
        },
    }

    model = "gemini-2.0-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"success": True, "text": text, "error": ""}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        return {"success": False, "text": "", "error": f"HTTP {e.code}: {error_body}"}
    except Exception as e:
        return {"success": False, "text": "", "error": str(e)}


def generate_answer(query: str, context: str, chat_history: list[dict] = None) -> dict:
    """
    High-level function: build messages from history + current query, call API.
    chat_history: list of {"role": "user"/"assistant", "content": str}
    """
    messages = []

    # Add prior turns (limit to last 6 turns to avoid token overflow)
    if chat_history:
        messages.extend(chat_history[-6:])

    # Add current RAG prompt
    messages.append({
        "role": "user",
        "content": build_rag_prompt(query, context),
    })

    return call_gemini_api(messages)
