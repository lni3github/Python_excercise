from fastapi import FastAPI
from pydantic import BaseModel

class BodyCreate(BaseModel):
    title : str
    author : str
    category : str

class BodyUpdate(BaseModel):
    id : int
    title : str
    author : str
    category : str

app = FastAPI()

# New
BOOKS = [
    {
        "id" : 1, 
        "title" : "Book One", 
        "author" : "Author One", 
        "category" : "Science"
    },
    {
        "id" : 2, 
        "title" : "Book Two", 
        "author" : "Author Two", 
        "category" : "Math"
    },
    {
        "id" : 3, 
        "title" : "Book Three", 
        "author" : "Author Three", 
        "category" : "History"
    },
]

@app.get("/books")
async def read_all_book():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book_byID(book_id:int):
    for book in BOOKS:
        if book.get("id") == book_id:
            return book
            
@app.post("/books/create_books")
async def create_book(book:BodyCreate):
    if BOOKS:
        last_book = BOOKS[-1]
    else:
        last_book = 0
    if not last_book:
        last_book =  BOOKS[0]
    book = { "id" : int(last_book.get("id"))+1, 
        "title" : book.title, 
        "author" : book.author, 
        "category" : book.category}
    BOOKS.append(book)
    return BOOKS   

@app.put("/books/update_books")
async def update_book(book_update:BodyUpdate):
    for i in range(len(BOOKS)):
        if str(BOOKS[i].get("id")) == str(book_update.id):
            BOOKS[i] = book_update
            return BOOKS
    return None

@app.delete("/books/delete_books/{id}")
async def update_book(id):
    for i in range(len(BOOKS)):
        if str(BOOKS[i].get("id")) == str(id):
            BOOKS.pop(i)
            break
    return None

  
