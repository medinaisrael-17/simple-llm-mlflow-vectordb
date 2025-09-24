# Simple FAISS integration

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorDB:
    # dim is the dimension of our vectors, or how long each embedding is.
    # our FAISS needs to know this in order to store and compare vectors correctly. 
    def __init__(self, embedding_model="all-MiniLM-L6-v2", dim=384):
        self.embedder = SentenceTransformer(embedding_model)
        # Flat means it stores all vectors in memory in a simple, linear array.
        # No fancy trees or clustering.
        # L2 refers to a distance metric used L2 = Euclidean distance. 
        # Finds what is closest in Eucledian Space. 
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, docs):
        embeddings = self.embedder.encode(docs)
        self.index.add(np.array(embeddings)) # add our document vectors.
        self.documents.extend(docs)

    def query(self, text, top_k=3):
        embedding = self.embedder.encode([text])
        D, I = self.index.search(np.array(embedding), top_k) # D = distance to the closest vectors I = indicies of the closest vectores in stored data.
        return [self.documents[i] for i in I[0]]

