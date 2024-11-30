from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document


# embeddings = OllamaEmbeddings(
#     model="nomic-embed-text ",
# )

llm = OllamaLLM(model="llama3.2:1b")
llm.invoke("The first man on the moon was ...")


# See docker command above to launch a postgres instance with pgvector enabled.

# conn = psycopg2.connect(host='localhost', user='postgres',password='example', dbname='postgres', port=5555)
# conn = psycopg2.connect("postgresql://postgres:example@localhost:5555/postgres")

connection = "postgresql+psycopg://postgres:example@localhost:5555/postgres"  # Uses psycopg3!

collection_name = "my_docs"

vector_store = PGVector(
    embeddings=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

document_1 = Document(page_content="foo", metadata={"baz": "bar"})
document_2 = Document(page_content="thud", metadata={"bar": "baz"})
document_3 = Document(page_content="i will be deleted :(")

documents = [document_1, document_2, document_3]
ids = ["1", "2", "3"]
vector_store.add_documents(documents=documents, ids=ids)

# vector_store.delete(ids=["3"])

results = vector_store.similarity_search(query="thud",k=1)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")

#results = vector_store.similarity_search(query="thud",k=1)
#for doc in results:
#   print(f"* {doc.page_content} [{doc.metadata}]")
