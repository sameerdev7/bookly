from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException 
from src.books.book_data import books 
from src.books.schemas import Book, BookUpdateModel
from typing import List

book_router = APIRouter()

@book_router.get('/books', response_model=List[Book])
async def get_all_books():
    return books


@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: Book):
    books.append(book_data.model_dump())
    return book_data


@book_router.get('/{book_id}', response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@book_router.patch('/{book_id}', response_model=Book)
async def update_book(book_id: int, book_update_data: BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            update_data = book_update_data.model_dump(exclude_unset=True)
            book.update(update_data)
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return None
    raise HTTPException(status_code=404, detail="Book not found")

