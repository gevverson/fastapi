from fastapi import APIRouter, Depends
from routers import auth, todos
from company import companyapis,dependencies

# --- THIS IS THE FIX ---
# Add the 'tags' parameter to organize Swagger
router=APIRouter(
    prefix="/companyapis",
    tags=["Company APIs"],
    dependencies=[Depends(dependencies.get_token_header)]
)

@router.get("/")
async def get_company_name():
    return{"company_name":"Gevverson Company,LLC"}


# --- THIS IS THE FIX ---
# The decorator must be on the line directly above the function
@router.get("/employees")
async def number_of_employees():
    return 163