import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAISSMemory:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.text_store = []

    def store(self, text):
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding, dtype='float32'))
        self.text_store.append(text)

    def retrieve(self, query, k=3):
        embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(embedding, dtype='float32'), k)
        return [self.text_store[i] for i in indices[0]]
