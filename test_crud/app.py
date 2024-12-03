from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from test_crud.schemas import BookDB, BookList, BookSchema, Message

app = FastAPI()

# test database
database = []


@app.post("/books/", status_code=HTTPStatus.CREATED, response_model=BookSchema)  # type: ignore
def create_book(books: BookSchema):
    book_with_id = BookDB(**books.model_dump(), id=len(database) + 1)

    database.append(book_with_id)
    return book_with_id


@app.get("/books/", response_model=BookList)
def read_books():
    return {"books": database}


@app.put("/books/{book_id}", response_model=BookSchema)
def update_book(book_id: int, book: BookSchema):
    if book_id > len(database) or book_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Book not found"
        )

    book_with_id = BookDB(**book.model_dump(), id=book_id)
    database[book_id - 1] = book_with_id

    return book_with_id


@app.delete("/books/{book_id}", response_model=Message)
def delete_book(book_id: int):
    if book_id > len(database) or book_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Book not found"
        )

    del database[book_id - 1]

    return {"message": "Book deleted"}


"""
POST: comunica com o servidor que enviara dados para ele aceitar, enviado pelo cliente.
GET: recuperar informação do servidor.
PUT: informar alteração nos dados para o servidor.
DELETE: deletar um determinado recurso.    
"""


'''
200 OK: Indica sucesso na requisição.
GET: Quando um dado é solicitado e retornado com sucesso.
PUT: Quando dados são alterados com sucesso.
201 CREATED: Significa que a solicitação resultou na criação de um novo recurso.
POST: Aplicável quando um dado é enviado e criado com sucesso.
PUT: Usado quando uma alteração resulta na criação de um novo recurso.
204 NO CONTENT: Retorno do servidor sem conteúdo na mensagem.
PUT: Aplicável se a alteração não gerar um retorno.
DELETE: Usado quando a ação de deletar não gera um retorno.
'''
