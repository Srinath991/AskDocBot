from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.pipelines.document_handler import process_document
from src.pipelines.query_handler import handle_query

app = FastAPI()

# Mount static folders
app.mount("/css", StaticFiles(directory="app/static/css"), name="css")
app.mount("/js", StaticFiles(directory="app/static/js"), name="js")

# Set up templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def home(request: Request):
    """Render the homepage."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    """Handle document uploads."""
    content = await file.read()
    response = process_document(content,index_name='demo')
    return {"message": "Document uploaded and processed", "details": response}

@app.get("/query/")
async def query(question: str):
    """Handle queries to the Q&A system."""
    answer = handle_query(question,index_name='demo')
    return {"question": question, "answer": answer}
