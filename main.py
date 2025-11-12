from fastapi import FastAPI,Depends
import models
from database import engine

# --- CORRECTED IMPORTS ---
# Import all our routers
from routers import auth, todos,address
from company import companyapis,dependencies

app = FastAPI()

# --- ROUTER INCLUDES ---
# Include all three routers. FastAPI will get the tags from each.
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(companyapis.router)

models.Base.metadata.create_all(bind=engine)

# ALL YOUR TODO ENDPOINTS ARE NOW IN 'routers/todos.py'
# This file is now clean and finished.