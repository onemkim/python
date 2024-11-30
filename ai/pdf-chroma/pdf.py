from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import sys

def ingest():
    # Get the doc
    loader = PyPDFLoader("toyota.pdf")
    pages = loader.load_and_split()
    # Split the pages by char
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(pages)
    print(f"Split {len(pages)} documents into {len(chunks)} chunks.")
    #
    embedding = FastEmbedEmbeddings()
    #Create vector store
    Chroma.from_documents(documents=chunks,  embedding=embedding, persist_directory="./sql_chroma_db")

# only run this once to generate vector store
ingest()

from huggingface_hub import login
access_token_read = "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"
access_token_write = "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"
login(token = access_token_read)


def rag_chain():
    model = ChatOllama(model="llama3.2:1b")
    #
    prompt = PromptTemplate.from_template(
        """
        <s> [Instructions] You are a friendly assistant. Answer the question based only on the following context. 
        If you don't know the answer, then reply, No Context availabel for this question {input}. [/Instructions] </s> 
        [Instructions] Question: {input} 
        Context: {context} 
        Answer: [/Instructions]
        """
    )
    #Load vector store
    embedding = FastEmbedEmbeddings()
    vector_store = Chroma(persist_directory="./sql_chroma_db", embedding_function=embedding)

    #Create chain
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.5,
        },
    )

    document_chain = create_stuff_documents_chain(model, prompt)
    chain = create_retrieval_chain(retriever, document_chain)
    #
    return chain

print("Test")

def ask(query: str):
    #
    chain = rag_chain()
    # invoke chain
    result = chain.invoke({"input": query})
    # print results
    print(result["answer"])
    for doc in result["context"]:
        print("Source: ", doc.metadata["source"])