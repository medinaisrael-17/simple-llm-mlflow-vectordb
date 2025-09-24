# Defines LLM wrapper class

from transformers import pipeline

class SimpleLLM: 
    def __init__(self, model_name="google/flan-t5-small"):
        self.generator = pipeline("text2text-generation", model=model_name)

    def generate(self, prompt, max_length=50):
        # max_length limits how many tokens the model will generate to prevent
        # infitely running and creating long outputs.
        # 
        # num_return_sequences will return only one answer. Increasing the number woll increase the amount
        # of possible answers returned in a List of dicts. 
        #
        # The rest is List traversal
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]["generated_text"]