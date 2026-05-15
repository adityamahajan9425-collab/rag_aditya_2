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

    # ── DEBUG: API key check ──────────────────────────────────────────────
    if not api_key:
        print("[DEBUG] GEMINI_API_KEY is MISSING from environment variables.")
        print(f"[DEBUG] Available env vars containing 'KEY': "
              f"{[k for k in os.environ if 'KEY' in k.upper()]}")
        return {
            "success": False,
            "text": "",
            "error": "GEMINI_API_KEY not set. Please set it in your environment variables.",
        }

    masked_key = api_key[:6] + "..." + api_key[-4:] if len(api_key) > 10 else "***"
    print(f"[DEBUG] GEMINI_API_KEY found: {masked_key}  (length={len(api_key)})")

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
    print(f"[DEBUG] Request → model={model}  payload_size={len(data)} bytes  messages={len(messages)}")

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
            raw = resp.read().decode("utf-8")
            result = json.loads(raw)
            print(f"[DEBUG] Response OK — candidates={len(result.get('candidates', []))}")

            # Check for blocked / empty responses
            if not result.get("candidates"):
                block_reason = result.get("promptFeedback", {}).get("blockReason", "unknown")
                print(f"[DEBUG] No candidates returned. blockReason={block_reason}")
                return {
                    "success": False,
                    "text": "",
                    "error": f"Gemini returned no candidates. Block reason: {block_reason}",
                }

            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"success": True, "text": text, "error": ""}

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"[DEBUG] HTTP Error {e.code} from Gemini API")
        print(f"[DEBUG] Response body: {error_body[:1000]}")

        # Try to parse structured error from Gemini
        detail_msg = error_body
        try:
            err_json = json.loads(error_body)
            detail_msg = err_json.get("error", {}).get("message", error_body)
            err_status = err_json.get("error", {}).get("status", "")
            print(f"[DEBUG] Error status={err_status}  message={detail_msg}")
        except json.JSONDecodeError:
            pass

        return {"success": False, "text": "", "error": f"HTTP {e.code}: {detail_msg}"}

    except Exception as e:
        print(f"[DEBUG] Unexpected exception: {type(e).__name__}: {e}")
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
