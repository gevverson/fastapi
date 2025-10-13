from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Coding with Gevverson', 'author': 'Sir Gevverson Kings'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


# ============= ROUTES IN CORRECT ORDER =============

# 1. Root endpoint
@app.get("/")
async def read_all_books():
    return BOOKS


# 2. SPECIFIC routes FIRST (before dynamic routes)
@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}


# 3. Directions endpoint (specific path)
@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}


# 4. Get book by ID (specific path with /books/)
@app.get("/books/{book_id}")
async def read_book_by_id(book_id: int):
    return {"book_title": book_id}


# 5. Search book by name (NEW - what you wanted!)
@app.get("/books/search/{book_name}")
async def search_book_by_name(book_name: str):
    """
    Search for book by name in the title
    Example: /books/search/title one
    """
    search_term = book_name.lower()
    
    # Search through all books
    matching_books = {}
    for book_key, book_data in BOOKS.items():
        if search_term in book_data['title'].lower():
            matching_books[book_key] = book_data
    
    if not matching_books:
        raise HTTPException(
            status_code=404,
            detail=f"No books found with '{book_name}' in title"
        )
    
    return {"results": matching_books}


# 6. Get book by exact key (LAST - most generic)
@app.get("/{book_name}")
async def read_book_by_key(book_name: str):
    """
    Get book by exact key (book_1, book_2, etc.)
    Example: /book_1
    """
    if book_name not in BOOKS:
        raise HTTPException(
            status_code=404,
            detail=f"Book key '{book_name}' not found"
        )
    return BOOKS[book_name]