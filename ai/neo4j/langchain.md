# ollama

## setup
Reference: https://python.langchain.com/docs/integrations/providers/ollama/

``` sh
# Ollama will start as a background service automatically, if this is disabled, run:

# export OLLAMA_HOST=127.0.0.1 # environment variable to set ollama host
# export OLLAMA_PORT=11434 # environment variable to set the ollama port
ollama serve

#After starting ollama, run ollama pull <model_checkpoint> to download a model from the Ollama model library.
ollama pull llama3.2

# We're now ready to install the langchain-ollama partner package and run a model.
# Ollama LangChain partner package install
#Install the integration package with:
pip install langchain-ollama
# for conda https://anaconda.org/conda-forge/langchain  only langchain package
conda install conda-forge::langchain
```


## Chat
Reference:
- https://python.langchain.com/docs/integrations/chat/ollama/

- Init
``` py
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    # other params...
)
```
- Invocation
``` py
from langchain_core.messages import AIMessage
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg
```


## Embedding
Reference: 
- https://python.langchain.com/docs/integrations/text_embedding/ollama/
- https://python.langchain.com/api_reference/ollama/embeddings/langchain_ollama.embeddings.OllamaEmbeddings.html#

``` sh
# Install
pip install -qU langchain-ollama
```

- init 
``` py
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
)
```

- indexing in vector store
``` py
# Create a vector store with a sample text
from langchain_core.vectorstores import InMemoryVectorStore

text = "LangChain is the framework for building context-aware reasoning applications"

vectorstore = InMemoryVectorStore.from_texts(
    [text],
    embedding=embeddings,
)

# Use the vectorstore as a retriever
retriever = vectorstore.as_retriever()

# Retrieve the most similar text
retrieved_documents = retriever.invoke("What is LangChain?")

# show the retrieved document's content
retrieved_documents[0].page_content
```

- Direct query
``` py
single_vector = embeddings.embed_query(text)
print(str(single_vector)[:100])  # Show the first 100 characters of the vector
```