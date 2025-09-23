# Defines LLM wrapper class

from transformers import pipeline

class SimpleLLM: 
    def __init__(self, model_name="google/flan-t5-small"):
        self.generator = pipeline("text2text-generation", model=model_name)

    def generate(self, prompt, max_length=50):
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]["generated_text"]