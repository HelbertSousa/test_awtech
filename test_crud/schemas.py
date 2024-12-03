from pydantic import BaseModel


class Message(BaseModel):
    message: str


class BookSchema(BaseModel):
    title: str
    autor: str
    category: str

'''
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
);
'''

class BookDB(BookSchema):
    id: int


class BookList(BaseModel):
    users: list[BookSchema]


# Schema:
"""{
    "title": "A gaia ciencia",
    "autor": "Nietzsche",
    "category": "filosofia"
}
"""
