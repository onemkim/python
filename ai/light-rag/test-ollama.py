import os
from lightrag import LightRAG, QueryParam
# from lightrag.llm import gpt_4o_mini_complete, gpt_4o_complete
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()
#########

WORKING_DIR = "./books"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# rag = LightRAG(
#    # working_dir=WORKING_DIR,
#    # llm_model_func=gpt_4o_mini_complete  # Use gpt_4o_mini_complete LLM model
#     llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
# )

# Initialize LightRAG with Ollama model
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,  # Use Ollama model for text generation
    llm_model_name='llama3.2', # Your model name
    # Use Ollama embedding function
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(
            texts,
            embed_model="nomic-embed-text"
        )
    ),
)

with open("./a_christmas_carol.txt") as f:
    rag.insert(f.read())

# Perform naive search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="naive")))

# Perform local search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="local")))

# Perform global search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="global")))

# Perform hybrid search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid")))