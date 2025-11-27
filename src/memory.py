import os
import json
from typing import Any, Dict, List, Tuple, Optional
import faiss
import numpy as np

from .utils import embed_texts, embed_query


class VectorMemory:
    """
    A lightweight FAISS-backed memory for storing and retrieving task and context entries.
    Persists index and metadata to local files for reuse across sessions.
    """

    def __init__(self, index_path: str = "memory.index", meta_path: str = "memory_meta.json", dim: int = 768):
        self.index_path = index_path
        self.meta_path = meta_path
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)
        self.metadata: Dict[int, Dict[str, Any]] = {}
        self._next_id = 0
        self._load_if_available()

    def _load_if_available(self) -> None:
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        if os.path.exists(self.meta_path):
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            self.metadata = {int(k): v for k, v in meta.get("metadata", {}).items()}
            self._next_id = meta.get("next_id", len(self.metadata))

    def _persist(self) -> None:
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "w", encoding="utf-8") as f:
            json.dump({"metadata": self.metadata, "next_id": self._next_id}, f, ensure_ascii=False, indent=2)

    def add_texts(self, texts: List[str], metadatas: Optional[List[Dict[str, Any]]] = None) -> List[int]:
        embeddings = embed_texts(texts)
        vecs = np.array(embeddings, dtype="float32")
        faiss.normalize_L2(vecs)
        self.index.add(vecs)

        ids = []
        for i, text in enumerate(texts):
            rid = self._next_id
            ids.append(rid)
            self.metadata[rid] = {
                "text": text,
                "meta": (metadatas[i] if metadatas and i < len(metadatas) else {}),
            }
            self._next_id += 1
        self._persist()
        return ids

    def search(self, query: str, top_k: int = 5) -> List[Tuple[int, float, Dict[str, Any]]]:
        q = np.array([embed_query(query)], dtype="float32")
        faiss.normalize_L2(q)
        scores, idxs = self.index.search(q, top_k)
        results = []
        for i, score in zip(idxs[0], scores[0]):
            if i == -1:
                continue
            results.append((int(i), float(score), self.metadata.get(int(i), {})))
        return results

    def get(self, rid: int) -> Dict[str, Any]:
        return self.metadata.get(rid, {})
