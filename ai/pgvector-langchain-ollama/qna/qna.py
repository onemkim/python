from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings

def process_data():
    print("Getting data...")
    loader = DirectoryLoader(path="/Users/minkim/Documents/git/onemkim/python/ai/pgvector-langchain-ollama/qna/documents", glob="**/*.txt")
    documents = loader.load()
    print("Documents loaded.")
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    print("Text splitted.")
    
    texts = text_splitter.split_documents(documents)
    
    print(texts)
    
    return texts

def create_retriever():
    
    connection = "postgresql+psycopg://postgres:example@localhost:5555/postgres" 
    collection_name = "qna"
    
    texts = process_data() 
    vector_store = PGVector.from_documents (
        documents=texts, 
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        collection_name=collection_name,
        connection=connection,
        use_jsonb=True,
    )   
    print("Vector store created.")

    model = OllamaLLM(model="llama3.2:1b")

    qna_retriever = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    
    return qna_retriever

def query(prompt, qna_retriever):
    print(f"Answer: {qna_retriever.run(prompt)}")

if __name__ == '__main__':    
    load_dotenv()
    
    qna_retriever = create_retriever()

    while True:
        prompt = input("Prompt: ")
        
        if prompt == "":
            break
        
        query(prompt, qna_retriever)
        cont = input("Press 'Enter' to prompt again.\n")
        
        if cont != "":
            break