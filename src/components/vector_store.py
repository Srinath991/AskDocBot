import sys
from pinecone import Pinecone
from langchain_pinecone.vectorstores import PineconeVectorStore
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv

load_dotenv()

PINECONE = Pinecone()

def get_pinecone_vector_store(index_name:str,embeddings:str,**kwargs):
    try:
        index = PINECONE.Index(index_name)
        return  PineconeVectorStore(index=index, embedding=embeddings,**kwargs)
    except Exception as e:
        raise CustomException(e,sys)

    
    