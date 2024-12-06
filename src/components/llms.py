from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logging
import sys
load_dotenv()
from langchain_google_genai import GoogleGenerativeAI

def get_google_llm(model='gemini-1.5-pro',**kwargs):
    try:
        return GoogleGenerativeAI(model=model,**kwargs)
    except Exception as e:
        raise CustomException(e,sys)