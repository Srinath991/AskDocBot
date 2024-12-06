from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import users
app = FastAPI()

# Mount static folders
app.mount("/css", StaticFiles(directory="app/static/css"), name="css")
app.mount("/js", StaticFiles(directory="app/static/js"), name="js")
templates = Jinja2Templates(directory="app/templates")

app.include_router(users.router,prefix='/api/v1/user')

@app.get("/")
async def home(request: Request):
    """Render the homepage."""
    return templates.TemplateResponse("index.html", {"request": request})