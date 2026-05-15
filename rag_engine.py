"""
RAG Engine
Handles: document chunking, TF-IDF vectorisation, cosine similarity retrieval
No external API required for retrieval — pure Python + NumPy
"""

import re
import math
import numpy as np
from knowledge_base import get_all_missions


# ─── Text Chunking ─────────────────────────────────────────────────────────────

def chunk_text(text: str, chunk_size: int = 400, overlap: int = 80) -> list[str]:
    """Split text into overlapping chunks by word count."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        if len(chunk.strip()) > 30:
            chunks.append(chunk.strip())
        if end >= len(words):
            break
        start += chunk_size - overlap
    return chunks


# ─── TF-IDF Vectorizer ─────────────────────────────────────────────────────────

class TFIDFVectorizer:
    def __init__(self):
        self.vocabulary: dict[str, int] = {}
        self.idf: np.ndarray = None
        self.fitted = False

    @staticmethod
    def tokenize(text: str) -> list[str]:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        tokens = text.split()
        # Remove very short tokens and common stopwords
        stopwords = {
            "the", "a", "an", "is", "it", "in", "on", "at", "of", "to", "and",
            "or", "for", "with", "as", "by", "this", "that", "was", "are",
            "its", "be", "has", "have", "had", "been", "were", "from", "but",
            "also", "not", "will", "can", "than", "into", "more", "over",
            "each", "their", "them", "they", "which", "who", "all", "one",
        }
        return [t for t in tokens if len(t) > 2 and t not in stopwords]

    def fit(self, documents: list[str]):
        # Build vocabulary
        word_doc_count: dict[str, int] = {}
        tokenized_docs = [self.tokenize(doc) for doc in documents]

        vocab_set = set()
        for tokens in tokenized_docs:
            vocab_set.update(tokens)
            for token in set(tokens):
                word_doc_count[token] = word_doc_count.get(token, 0) + 1

        self.vocabulary = {word: idx for idx, word in enumerate(sorted(vocab_set))}

        # Compute IDF
        n_docs = len(documents)
        idf_values = []
        for word in sorted(vocab_set):
            df = word_doc_count.get(word, 0)
            idf_values.append(math.log((n_docs + 1) / (df + 1)) + 1)

        self.idf = np.array(idf_values)
        self.fitted = True

    def transform(self, texts: list[str]) -> np.ndarray:
        if not self.fitted:
            raise RuntimeError("Vectorizer not fitted. Call fit() first.")

        n = len(texts)
        v = len(self.vocabulary)
        matrix = np.zeros((n, v))

        for i, text in enumerate(texts):
            tokens = self.tokenize(text)
            if not tokens:
                continue
            token_counts: dict[str, int] = {}
            for token in tokens:
                token_counts[token] = token_counts.get(token, 0) + 1
            max_count = max(token_counts.values())
            for token, count in token_counts.items():
                if token in self.vocabulary:
                    j = self.vocabulary[token]
                    tf = count / max_count
                    matrix[i][j] = tf * self.idf[j]

        # L2 normalise
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1, norms)
        matrix = matrix / norms
        return matrix

    def fit_transform(self, texts: list[str]) -> np.ndarray:
        self.fit(texts)
        return self.transform(texts)


# ─── Document Store ────────────────────────────────────────────────────────────

class DocumentChunk:
    def __init__(self, chunk_id: int, text: str, mission_id: str,
                 mission_title: str, agency: str, chunk_index: int):
        self.chunk_id = chunk_id
        self.text = text
        self.mission_id = mission_id
        self.mission_title = mission_title
        self.agency = agency
        self.chunk_index = chunk_index

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "mission_id": self.mission_id,
            "mission_title": self.mission_title,
            "agency": self.agency,
            "chunk_index": self.chunk_index,
        }


class RAGEngine:
    def __init__(self):
        self.chunks: list[DocumentChunk] = []
        self.vectorizer = TFIDFVectorizer()
        self.chunk_vectors: np.ndarray = None
        self._build_index()

    def _build_index(self):
        missions = get_all_missions()
        chunk_texts = []

        for mission in missions:
            # Combine metadata into searchable text
            full_text = (
                f"{mission['title']} {mission['agency']} {mission['type']} "
                f"{mission['launch_date']} {' '.join(mission.get('tags', []))} "
                f"{mission['content']}"
            )
            raw_chunks = chunk_text(full_text, chunk_size=150, overlap=30)
            for i, raw in enumerate(raw_chunks):
                dc = DocumentChunk(
                    chunk_id=len(self.chunks),
                    text=raw,
                    mission_id=mission["id"],
                    mission_title=mission["title"],
                    agency=mission["agency"],
                    chunk_index=i,
                )
                self.chunks.append(dc)
                chunk_texts.append(raw)

        # Fit vectorizer and compute embeddings
        self.chunk_vectors = self.vectorizer.fit_transform(chunk_texts)
        print(f"[RAG] Indexed {len(self.chunks)} chunks from {len(missions)} missions.")

    def retrieve(self, query: str, top_k: int = 5, agency_filter: str = None
                 ) -> list[tuple[DocumentChunk, float]]:
        """Return (chunk, score) pairs for the query."""
        query_vec = self.vectorizer.transform([query])[0]
        scores = self.chunk_vectors @ query_vec  # cosine similarity (vectors are normalised)

        # Apply agency filter
        if agency_filter:
            for i, chunk in enumerate(self.chunks):
                if chunk.agency.upper() != agency_filter.upper():
                    scores[i] = -1.0

        top_indices = np.argsort(scores)[::-1][:top_k * 3]  # over-fetch for dedup

        # Deduplicate: max 2 chunks per mission
        seen_missions: dict[str, int] = {}
        results = []
        for idx in top_indices:
            if scores[idx] <= 0:
                continue
            chunk = self.chunks[idx]
            count = seen_missions.get(chunk.mission_id, 0)
            if count < 2:
                results.append((chunk, float(scores[idx])))
                seen_missions[chunk.mission_id] = count + 1
            if len(results) >= top_k:
                break

        return results

    def get_context_for_prompt(self, query: str, top_k: int = 5,
                               agency_filter: str = None) -> tuple[str, list[dict]]:
        """
        Returns (formatted_context_string, list_of_source_dicts)
        Sources list is used to display citations in the UI.
        """
        results = self.retrieve(query, top_k=top_k, agency_filter=agency_filter)
        if not results:
            return "", []

        context_parts = []
        sources = []
        seen_ids = set()

        for i, (chunk, score) in enumerate(results):
            source_label = f"[Source {i+1}]"
            context_parts.append(f"{source_label} From: {chunk.mission_title} ({chunk.agency})\n{chunk.text}")

            # Deduplicate sources for citation list
            if chunk.mission_id not in seen_ids:
                sources.append({
                    "label": source_label,
                    "title": chunk.mission_title,
                    "agency": chunk.agency,
                    "mission_id": chunk.mission_id,
                    "relevance_score": round(score, 4),
                    "preview": chunk.text[:200] + "..." if len(chunk.text) > 200 else chunk.text,
                })
                seen_ids.add(chunk.mission_id)

        context_str = "\n\n---\n\n".join(context_parts)
        return context_str, sources


# ─── Singleton ────────────────────────────────────────────────────────────────
_engine_instance = None

def get_engine() -> RAGEngine:
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = RAGEngine()
    return _engine_instance
