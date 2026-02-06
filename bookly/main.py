from fastapi import FastAPI, status 
from fastapi.exceptions import HTTPException 
from src.books.book_data import books 
from src.books.schemas import Book, BookUpdateModel

from typing import List

app = FastAPI()



# Lec 1 
# @app.get("/")
# async def hello():
#     return {"message": "hello world"}

# @app.get('/greet')
# async def greet_name(name:Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"hello {name}", "age": age}

# class BookCreateModel(BaseModel):
#     title : str
#     author : str 

# @app.post('/create_book')
# async def create_book(book_data: BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }


# @app.get('/get_headers', status_code=500)
# async def get_headers(
#     accept:str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_headers = {}
#     request_headers["Accept"] = accept 
#     request_headers["Content-Type"] = content_type
#     request_headers["User-Agent"] = user_agent
#     request_headers["HOST"] = host

#     return request_headers