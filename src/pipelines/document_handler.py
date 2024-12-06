import sys
import io
from src.exception import CustomException
from src.logger import logging
from src.components.embeddings import get_embeddings
from src.components.vector_store import get_pinecone_vector_store
from src.components.text_splitter import chunk_data
from langchain_community.document_loaders import PyPDFLoader
def process_document(content,index_name,**kwargs):
    try:
        loader = PyPDFLoader(file_path='/Users/apple/Downloads/@vtucode.in-21CS644-module-5-2021-scheme (1).pdf')
        documents = loader.load()
        docs=chunk_data(documents,chunk_size=100,chunk_overlap=20)
        embeddings=get_embeddings()
        vector_store=get_pinecone_vector_store(index_name,embeddings)
        return vector_store.from_documents(docs,embedding=embeddings,index_name=index_name)
    except Exception as e:
        raise CustomException(e,sys)
    
    
    