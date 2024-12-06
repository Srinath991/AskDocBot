from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from src.components.llms import pc

from langchain_pinecone.vectorstores import PineconeVectorStore

def handle_query(query:str):
    
    llm=GoogleGenerativeAI(model='gemini-1.5-pro',temperature=0.8)
    index_name ='langchainvector'
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    retriever=vector_store.as_retriever(search_kwargs={'k': k})
    pass