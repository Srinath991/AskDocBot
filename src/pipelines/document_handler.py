import sys
from src.exception import CustomException
from src.components.embeddings import get_embeddings
from src.components.vector_store import get_pinecone_vector_store
from src.components.text_splitter import chunk_data
from langchain_community.document_loaders import PyPDFLoader
import tempfile
def process_document(content,index_name,**kwargs):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            tmpfile.write(content)  # Write the byte content to the temporary file
            tmpfile_path = tmpfile.name 
        loader=PyPDFLoader(tmpfile_path)
        pages = []
        for page in loader.lazy_load():
                pages.append(page)
        docs=chunk_data(pages,chunk_size=1000,chunk_overlap=200)
        embeddings=get_embeddings()
        vector_store=get_pinecone_vector_store(index_name,embeddings)
        vector_store.from_documents(docs,embedding=embeddings,index_name=index_name)
        return vector_store
    except Exception as e:
        raise CustomException(e,sys)
    
    
    