from fastapi import APIRouter,Request,UploadFile,File
from src.pipelines.document_handler import process_document
from src.pipelines.query_handler import handle_query
import os
router=APIRouter()
# Set up templates


@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    """Handle document uploads."""
    content=await file.read()
    response = process_document(content, index_name='demo')
    return {"message": "Document uploaded and processed", "details": response}


@router.get("/query/")
async def query(question: str):
    """Handle queries to the Q&A system."""
    answer = handle_query(question,index_name='demo')
    return {"question": question, "answer": answer}
