from dataclasses import dataclass
from datetime import date

@dataclass
class Nationality:
    code: str
    name: str

@dataclass
class Autor:
    name: str
    date_of_birth: date
    bibliographic_note: str
    nationality: Nationality
    code: int = None

@dataclass
class Publisher:
    name: str
    phone: str
    address: str
    code: int = None

@dataclass
class Language:
    code: str
    name: str

@dataclass
class Edition:
    isbn: str
    price: float
    year: int
    stock_quantity: int
    num_pages: int
    publisher: Publisher

@dataclass
class Book:
    title: str
    year: int 
    language: Language
    editions: list[Edition]
    code: int = None