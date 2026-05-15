# 🛸 AstroRAG — Space Mission Intelligence Chatbot

> **RAG-powered AI assistant for ISRO & NASA mission reports**  
> SISTec Gandhi Nagar · Build with RAG Workshop · Problem Statement #10

---

## 📌 Problem Statement

**Domain:** Science Explainer  
**Task:** Build a RAG assistant over ISRO or NASA mission reports to answer questions about mission objectives, instruments, outcomes, and timelines with cited source chunks.  
**Evaluation Focus:** Scientific accuracy, source citation, explanation quality, presentation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      User Query                         │
└─────────────────────┬───────────────────────────────────┘
                      │
         ┌────────────▼────────────┐
         │   TF-IDF Vectorizer     │  ◄── Tokenise + Compute
         │   (rag_engine.py)       │       TF-IDF scores
         └────────────┬────────────┘
                      │  Cosine Similarity Search
         ┌────────────▼────────────┐
         │   Document Chunks       │  ◄── Pre-indexed from
         │   (Vector Index)        │       knowledge_base.py
         └────────────┬────────────┘
                      │  Top-K relevant chunks
         ┌────────────▼────────────┐
         │   Context Assembly      │  ◄── Source attribution
         │   + Citation Labels     │       [Source 1], [Source 2]...
         └────────────┬────────────┘
                      │  Prompt with context
         ┌────────────▼────────────┐
         │   Claude Sonnet API     │  ◄── Answer generation
         │   (llm_client.py)       │       with multi-turn memory
         └────────────┬────────────┘
                      │
         ┌────────────▼────────────┐
         │   Streamlit UI / CLI    │  ◄── Cited answer +
         │   (app.py / cli_demo.py)│       source cards
         └─────────────────────────┘
```

---

## 📚 Knowledge Base

12 missions across ISRO and NASA:

| Mission | Agency | Type | Status |
|---------|--------|------|--------|
| Chandrayaan-1 | ISRO | Lunar Orbiter | Completed |
| Chandrayaan-2 | ISRO | Orbiter+Lander+Rover | Partial Success |
| **Chandrayaan-3** | **ISRO** | **Lander+Rover** | **✅ Successful** |
| Mangalyaan (MOM) | ISRO | Mars Orbiter | Completed (8 yrs) |
| Aditya-L1 | ISRO | Solar Observatory | 🟢 Active |
| Gaganyaan | ISRO | Human Spaceflight | 🔶 In Development |
| PSLV Program | ISRO | Launch Vehicle | 🟢 Active |
| **Artemis Program** | **NASA** | Crewed Lunar | 🟢 Active |
| James Webb ST | NASA | Space Telescope | 🟢 Active |
| Perseverance | NASA | Mars Rover | 🟢 Active |
| Parker Solar Probe | NASA | Solar Probe | 🟢 Active |
| Voyager 1 & 2 | NASA | Interstellar | 🟢 Active (~47 yrs) |

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd space_rag
pip install -r requirements.txt
```

### 2. Set API Key

```bash
# Linux/Mac
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows
set ANTHROPIC_API_KEY=sk-ant-...
```

### 3a. Run Web App (Streamlit)

```bash
streamlit run app.py
```
Opens at `http://localhost:8501`

### 3b. Run CLI Demo

```bash
# Interactive mode
python cli_demo.py

# Single query
python cli_demo.py "What did Chandrayaan-3 discover on the Moon?"

# Full demo (preset questions)
python cli_demo.py --demo
```

---

## 🔧 RAG Pipeline Details

### Document Chunking (`rag_engine.py`)
- Text split into ~400-word overlapping windows (80-word overlap)
- Each chunk tagged with mission metadata (agency, title, ID)

### Vectorisation (TF-IDF)
- Pure Python + NumPy — no external embedding API needed
- Custom stopword removal and tokenisation
- L2-normalised vectors for efficient cosine similarity

### Retrieval
- Cosine similarity search over all chunks
- Deduplication: max 2 chunks per mission to ensure diversity
- Optional agency filter (ISRO-only or NASA-only)

### Generation (Claude Sonnet API)
- Retrieved context injected into prompt with [Source N] labels
- System prompt enforces scientific accuracy and citation
- Multi-turn memory via chat history (last 6 turns)

---

## 📋 Evaluation Criteria Coverage

| Criterion | Implementation |
|-----------|---------------|
| **Scientific Accuracy** | Claude Sonnet with strict grounding in retrieved chunks |
| **Source Citation** | [Source N] labels in every answer + citation cards in UI |
| **Explanation Quality** | RAG context ensures factual, detailed explanations |
| **Presentation** | Streamlit dark space-themed UI with mission cards, stats |
| **Mission Objectives** | Structured per-mission data including all objectives |
| **Instruments** | Complete instrument lists for every mission |
| **Outcomes/Findings** | Key discoveries and scientific results included |
| **Timelines** | Detailed chronological timelines per mission |

---

## 📁 File Structure

```
space_rag/
├── app.py              # Streamlit web application
├── cli_demo.py         # Command-line interface
├── rag_engine.py       # TF-IDF vectoriser + retrieval engine
├── llm_client.py       # Anthropic Claude API wrapper
├── knowledge_base.py   # ISRO & NASA mission data (12 missions)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 💡 Sample Queries

- *"What did Chandrayaan-3 discover on the lunar south pole?"*
- *"How does Mangalyaan compare to NASA's Mars missions?"*
- *"What are the instruments on JWST and what has it found?"*
- *"Explain the Parker Solar Probe's record-breaking achievements"*
- *"What happened to Voyager spacecraft after leaving the solar system?"*
- *"What is the status of India's Gaganyaan human spaceflight mission?"*
- *"Compare ISRO and NASA approaches to lunar exploration"*

---

## 🏆 Team Note

This project demonstrates a complete RAG pipeline:
1. **Curated domain knowledge** (12 detailed mission reports)
2. **Lightweight local retrieval** (TF-IDF, no external APIs for retrieval)
3. **State-of-the-art generation** (Claude Sonnet)
4. **Production UI** (Streamlit with citation display)
5. **Multi-turn conversation** with memory
