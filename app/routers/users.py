from fastapi import APIRouter,UploadFile,File
from src.pipelines.document_handler import process_document
from src.pipelines.query_handler import handle_query

router=APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    """
    Handle document uploads.
    """
    content=await file.read()
    process_document(content, index_name='demo')
    return {"message": "Document uploaded and processed"}


@router.get("/query/")
async def query(question: str):
    """
    Handle queries to the Q&A system.
    """
    answer = handle_query(question,index_name='demo')
    return {"question": question, "answer": answer}
