from typing import Optional
from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(
        title="Description of the book",
        max_length=100,
        min_length=1
    )
    rating: int = Field(gt=-1, lt=101)
    
    class Config:
        schema_extra = {
            "example": {
                "id": "1199e27f-2695-7e65-90f4-cbffdfa0ff79",
                "title": "Computer Science Pro",
                "author": "CodingwithGevverson",
                "description": "A very nice description of a book",
                "rating": 87
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books():
    """Get all books - Sets up fake inventory if empty"""
    if len(BOOKS) < 1:
        create_books_no_api()
    return BOOKS


@app.get("/book_login")
async def book_login(
    book_id: int = Query(..., description="ID of the book to read (0-4)", ge=0, lt=5),
    username: str = Header(..., description="Username for authentication"),
    password: str = Header(..., description="Password for authentication")
):
    """
    Authenticate user and return requested book.
    
    Authentication:
    - Username must be: FastAPIUser
    - Password must be: test1234!
    
    Headers:
    - username: FastAPIUser
    - password: test1234!
    
    Query Parameters:
    - book_id: Index of book to read (0-4)
    """
    
    # Ensure books are initialized
    if len(BOOKS) < 1:
        create_books_no_api()
    
    # Check authentication
    if username != "FastAPIUser" or password != "test1234!":
        return {"message": "Invalid User"}
    
    # Validate book_id
    if book_id < 0 or book_id >= len(BOOKS):
        raise HTTPException(
            status_code=404,
            detail=f"Book with ID {book_id} not found. Valid IDs are 0-{len(BOOKS)-1}"
        )
    
    # Return the requested book
    return BOOKS[book_id]


@app.post("/")
async def create_book(book: Book):
    """Create a new book"""
    BOOKS.append(book)
    return book


def create_books_no_api():
    """Create fake book inventory"""
    book_1 = Book(
        id="0199e27f-2695-7e65-90f4-cbffdfa0ff79",  # type: ignore
        title="Computer Science Pro",
        author="CodingwithGevverson",
        description="A comprehensive guide to computer science",
        rating=60
    )
    book_2 = Book(
        id="1199e27f-2695-7e65-90f4-cbffdfa0ff79",  # type: ignore
        title="Python Programming",
        author="FastAPI Developer",
        description="Learn Python from scratch",
        rating=56
    )
    book_3 = Book(
        id="2199e27f-2695-7e65-90f4-cbffdfa0ff79",  # type: ignore
        title="Web Development Mastery",
        author="Tech Guru",
        description="Master web development skills",
        rating=76
    )
    book_4 = Book(
        id="3199e27f-2695-7e65-90f4-cbffdfa0ff79",  # type: ignore
        title="Data Science Handbook",
        author="Data Expert",
        description="Everything about data science",
        rating=89
    )
    book_5 = Book(
        id="4199e27f-2695-7e65-90f4-cbffdfa0ff79",  # type: ignore
        title="AI and Machine Learning",
        author="ML Master",
        description="Dive into AI and ML concepts",
        rating=90
    )

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    BOOKS.append(book_5)


   
