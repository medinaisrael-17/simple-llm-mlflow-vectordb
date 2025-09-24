# simple-llm-mlflow-vectordb
A simple LLM that's packaged with MLflow and stores Vectors in a VectorDB.

# Resources
- Interactive Python Notebook
- Jupyter Notebook
- MLflow
- Conda
- FAISS

# How To Run
In your terminal run 

### python run.py --question "Where is the Eiffel Tower?"

Optionals

- python run.py --question "Where is the Colosseum?"
- python run.py --question "Where is the Statue of Liberty?"

# How It Works
LLMs are the most popular tools used today by developers and people alike. With big names such as ChatGPT, DeepSeek, Llama, and many more, companies often ask for their own LLM that can invite new investors and consumers. In this repo I have created a small, mini LLM that can take questions for famous landmarks and tell the user the correct location by understanding the context of what the user is asking. 

`run.py` is the main script that will kick things off. Once a user has fired up the LLM, `run.py` will parse the question asked in the terminal and begin creating our pipeline. The pipeline first constructs our text generator which in this case will be Hugging Face's `google/flan-t5-small` model. This model will be used to generate a response based on the question that was asked. Next, it initializes our Vector Database that will house information using the `all-MiniLM-L6-v2` provided by the FAISS library. This library is great for completing fast, similarity searches in a high-dimensional vector space, or in this case, its great at finding the location of the landmark you are asking for! To see more of the specifics open `src/vector_store.py`. `run.py` then creates our vectors and adds them to our pipeline so our LLM knows the exact locations of three famous landmarks

- The Eiffel Tower
- The Colosseum
- The Statue of Liberty

Lastly, it puts everything together, </br>
> *parse the question*
>> *create and store vectors*
>>> *compare question to other vectors and find which is most similar*
>>>> *generate a response*
>>>>> *print to the terminal so the user can see*


# MLflow
MLflow is how computer scientists can maintain consistency and quality amongst ever changing ML Models and experiments. It acts as the DevOps equivalent but specifically for ML, allowing for models to be easily reproducible and easily tracked with logs, outputs, and parameters.

In this repo, under `mlflow_project/` is where the LLM model is packaged and can be used for other developers to work on the model on any machine or in any environment. `MLproject` defines which Conda environment to use and specifies which tasks can be executed with this LLM as well as any necessary parameters such as the landmark you are looking for. The `conda.yaml` lists all the dependencies this project uses. 

For those wishing to use MLflow with this project, once you have downloaded the repo and have conda installed on your machine or environment, please run the following command.

### mlflow run . -P question="Where is the Eiffel Tower?"

#### -Israel Medina 09.24.2025


