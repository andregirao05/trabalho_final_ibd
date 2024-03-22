"""
Classes que guardam os dados de entidades.
"""
from dataclasses import dataclass
from datetime import date

@dataclass
class Nationality:
    code: str
    name: str

@dataclass
class Author:
    name: str
    date_of_birth: date
    biographic_note: str
    nationality_code: str
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
    year: str
    stock_quantity: int
    num_pages: int
    publisher_code: int = None
    book_code: int = None

@dataclass
class Book:
    title: str
    year: str 
    language_code: str
    code: int = None
    author_code: int = None