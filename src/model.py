# Defines LLM wrapper class

from transformers import pipeline

class SimpleLLM: 
    def __init__(self, model_name="distilgpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt, max_length=50):
        return self.generator(prompt, max_length=max_length, num_return_sequence=1)[0]["generated_text"]