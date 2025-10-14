from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID




#from books import BOOKS


app=FastAPI()


class Book(BaseModel):
    id:UUID
    title:str =Field(min_length=1)
    author:str=Field(min_length=1,max_length=100)
    description:Optional[str]=Field(title="Description of the book",
                                    max_length=100,
                                    min_length=1)
    rating:int=Field(gt=-1,lt=101)



BOOKS=[]

@app.get("/")
async def read_all_books():
    if len(BOOKS)<1:
        create_books_no_api()

    return BOOKS



@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

def create_books_no_api():
    book_1=Book(id="0199e27f-2695-7e65-90f4-cbffdfa0ff79",
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=60)
    book_2=Book(id="1199e27f-2695-7e65-90f4-cbffdfa0ff79",
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=56)
    book_3=Book(id="2199e27f-2695-7e65-90f4-cbffdfa0ff79",
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=76)
    book_4=Book(id="3199e27f-2695-7e65-90f4-cbffdfa0ff79",
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=89)
    book_5=Book(id="4199e27f-2695-7e65-90f4-cbffdfa0ff79",
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=90)
    



    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    BOOKS.append(book_5)
    
























