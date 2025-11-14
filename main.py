import http
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # <-- Import for CSS/JS
import models
from database import engine

# Import all our routers from their respective files
from routers import auth, todos, address

app = FastAPI()

# --- Mount Static Files ---
# This serves files from your "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Templating Setup ---
# This tells FastAPI to look for HTML files in the "templates" folder
templates = Jinja2Templates(directory="templates")

# --- ROUTER INCLUDES ---
# Include all routers. FastAPI will get the tags from each.
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)

# This creates all your database tables
models.Base.metadata.create_all(bind=engine)


# --- Homepage Endpoint ---
# This will run when someone visits "http://127.0.0.1:8000/"
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # This finds "home.html" in your "templates" folder and returns it
    return templates.TemplateResponse("index.html", {"request": request})


# --- Add-Todo Page Endpoint ---
# This will run when someone visits "http://1...:8000/add-todo"
@app.get("/add-todo", response_class=HTMLResponse)
async def add_todo_page(request: Request):
    # This finds "add-todo.html" in your "templates" folder
    return templates.TemplateResponse("add-todo.html", {"request": request})