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




    class Config:
        json_schema_extra = {
            "example": {
                "id":"1199e27f-2695-7e65-90f4-cbffdfa0ff79",
                "title":"Computer Science Pro",
                "author":"CodingwithGevverson",
                "description":"A very nice description of a book",
                "rating":87,


            }
        }

    




BOOKS=[]

@app.get("/")
async def read_all_books(books_to_return:Optional[int]=None):
    if len(BOOKS)<1:
        create_books_no_api()

    if books_to_return and len(BOOKS)>=books_to_return > 0:
        i=1
        new_books=[]
        while i<=books_to_return:
            new_books.append(BOOKS[i-1])
            i+=1
        return new_books    

    return BOOKS




@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id==book_id:
            return x
    

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id:UUID,book:Book):
    counter=0

    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            BOOKS[counter-1]=book
            return BOOKS[counter-1]
        

@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter=0

    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            del BOOKS[counter-1]
            return f'ID:{book_id} deleted'


def create_books_no_api():
    book_1=Book(id="0199e27f-2695-7e65-90f4-cbffdfa0ff79", # type: ignore
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=60)
    book_2=Book(id="1199e27f-2695-7e65-90f4-cbffdfa0ff79", # type: ignore
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=56)
    book_3=Book(id="2199e27f-2695-7e65-90f4-cbffdfa0ff79", # type: ignore
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=76)
    book_4=Book(id="3199e27f-2695-7e65-90f4-cbffdfa0ff79", # type: ignore
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=89)
    book_5=Book(id="4199e27f-2695-7e65-90f4-cbffdfa0ff79", # type: ignore
                title="GEVVERSON",
                author="GEVVERSONKINGS",
                description="DESCRIPTION 1",
                rating=90)
    



    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    BOOKS.append(book_5)
    
























