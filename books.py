 
from typing import Optional
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


"""
# 1. Root endpoint
@app.get("/")
async def read_all_books(): # type: ignore
    
    Retrieve all books.

    This asynchronous function returns a collection of all books stored in the `BOOKS` variable.

    Returns:
        list: A list containing all the books.
    
    return BOOKS
"""

@app.get("/")
async def read_all_books(skip_book:Optional[str]=None): # type: ignore
    """
    Reads all books except the one specified to be skipped.

    Args:
        skip_book (str): The key of the book to skip. Defaults to "book_3".

    Returns:
        dict: A dictionary containing all books except the skipped one.
    """
    if skip_book:
        new_books=BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

"""
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


# 5. Search book by name 
@app.get("/books/search/{book_name}")
async def search_book_by_name(book_name: str):
    
    #Search for book by name in the title
    #Example: /books/search/title one
    
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
    
    #Get book by exact key (book_1, book_2, etc.)
    #Example: /book_1

    if book_name not in BOOKS:
        raise HTTPException(
            status_code=404,
            detail=f"Book key '{book_name}' not found"
        )
    return BOOKS[book_name]
"""

#####POST
@app.post("/")
async def create_book(book_title,book_author):
    current_book_id=0

    if len(BOOKS)>0:
        for book in BOOKS:
            x=int(book.split('_')[-1])
            if x>current_book_id:
                current_book_id=x

    BOOKS[f'book_{current_book_id+1}']={'title':book_title,"author":book_author}
    return BOOKS[f'book_{current_book_id+1}']            


###PUT

@app.put("/{book_name}")
async def update_book(book_name:str,book_title:str,book_author:str):
    book_information={'title':book_title,'author':book_author}
    BOOKS[book_name]=book_information
    return book_information


####DELETE
@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'




"""
Assignment

Here is your opportunity to keep learning!

Currently we are using Path Parameters for our API calls. Create two new APIs for our current application :)

1. Create a new read book function that uses query params instead of path params.

2. Create a new delete book function that uses query params instead of path params.
"""
@app.get("/assignment/")
async def read_book_assignment(book_name:str):
    return BOOKS[book_name]

@app.delete("/assignment/")
async def delete_book_assignment(book_name:str):
    del BOOKS[book_name]
    return BOOKS