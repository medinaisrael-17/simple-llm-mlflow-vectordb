# Puts it together: embeddings -> vector db -> query -> LLM
from .model import SimpleLLM
from .vector_store import VectorDB

class SimplePipeline:
    def __init__(self):
        self.llm = SimpleLLM()
        self.db = VectorDB()

    def add_docs(self, docs):
        self.db.add(docs)

    def query(self, question):
        context_docs = self.db.query(question)
        context = " ".join(context_docs)
        prompt = f"Answer the question using context:\nContext: {context}\nQuestion: {question}\nAnswer:"
        return self.llm.generate(prompt)