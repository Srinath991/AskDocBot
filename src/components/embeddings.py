from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logging
import sys
load_dotenv()

def get_embeddings(model='models/embedding-001', **kwargs):
    """
    Initialize Google Generative AI Embeddings with a specified model and arguments.
    
    Args:
        model (str): Model name for embeddings.
        **kwargs: Additional arguments for GoogleGenerativeAIEmbeddings (e.g., API key).
    
    Returns:
        GoogleGenerativeAIEmbeddings: Instance of the embeddings class.
    """
    try:
        return GoogleGenerativeAIEmbeddings(model=model, **kwargs)
    except Exception as e:
        raise CustomException(e,sys)
    
