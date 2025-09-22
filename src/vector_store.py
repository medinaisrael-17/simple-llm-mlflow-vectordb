# Simple FAISS integration

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorDB:
    def __init__(self, embedding_model="all-MiniLM-L6-v2", dim=384):
        self.embedder = SentenceTransformer(embedding_model)
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, docs):
        embeddings = self.embedder.encode(docs)
        self.index.add(np.array(embeddings))
        self.documents.extend(docs)

    def query(self, text, top_k=3):
        embedding = self.embedder.encode([text])
        D, I = self.index.search(np.array(embedding), top_k)
        return [self.documents[i] for i in I[0]]

