"""
    Funções que geram dados para preencher o banco de dados
"""

import pandas as pd
import os
from entities import (
    Nationality, 
    Language,
    Author,
    Publisher,
    Book,
    Edition
)

from faker import Faker
import random
from datetime import datetime

_PARENT_DIR = os.path.dirname(os.path.realpath(__file__))
_DATA_PATH = os.path.join(_PARENT_DIR, '..', 'data')

fake = Faker('pt-BR')

def generate_languages():
    """
        Função gera uma lista de objetos da classe Language usando dados do mundo real
        disponíveis em https://github.com/andregirao05/trabalho_final_ibd/blob/main/data/languages.csv.

        Os dados incluem: 
            - código do idioma no padrão ISO 639-2;
            - nome do idioma (em inglês).
    """
    data = pd.read_csv(os.path.join(_DATA_PATH, 'languages.csv'), index_col=None)
    data = data[['ISO 639-2 Code', 'English name of Language']]
    data['English name of Language'] = data['English name of Language'].apply(lambda x: x.split(';')[0])
    data['ISO 639-2 Code'] = data['ISO 639-2 Code'].apply(lambda x: x.split('-')[0])

    languages = [Language(row['ISO 639-2 Code'], row['English name of Language']) for _, row in data.iterrows()]

    return languages

def generate_nacionalities():
    """
        Cria uma lista de objetos da classe Nacionality com dados do mundo real
        disponíveis em https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

        Os dados incluem:
            - código do país no padrão ISO 3116-2
            - nome do país (em inglês)
    """
    data = pd.read_csv(os.path.join(_DATA_PATH, 'countries.csv'), keep_default_na=False)
    data = data[['alpha-2', 'name']]

    nacionalities = [Nationality(row['alpha-2'], row['name']) for _, row in data.iterrows()]

    return nacionalities

def generate_authors(number_of_authors = 20):
    """
        Gera uma lista de objetos da classe Author de tamanho especificado com dados aleatórios.
    """
    authors = []

    for i in range(number_of_authors):
        authors.append(Author(
            name=fake.name(),
            date_of_birth=datetime.strptime(fake.date(), "%Y-%m-%d"),
            biographic_note=fake.sentence(),
            nationality_code=fake.country_code()
        ))

    return authors

def generate_publishers(number_of_publishers = 20):
    """
        Gera uma lista de objetos da classe Publisher de tamanho especificado com dados aleatórios.
    """
    publishers = []

    for i in range(number_of_publishers):
        publishers.append(Publisher(
            name=fake.company(),
            phone=''.join(char for char in fake.phone_number() if char.isdigit() or char.isspace()), #número de telefone, apenas digitos e espaços brancos entre códigos
            address=fake.address()
        ))

    return publishers

def generate_books(author_code, number_of_books = 20):
    """
        Gera uma lista de objetos da classe Book de tamanho especificado com dados aleatórios.
    """
    language_code = random.choice(generate_languages()).code

    books = []
    for i in range(number_of_books):
        books.append(Book(
            title=fake.catch_phrase(),
            year=fake.year(),
            language_code=language_code,
            author_code=author_code
         ))
    
    return books

def generate_editions(publisher_code, number_of_editions = 20, book_code = None):
    """
        Gera uma lista de objetos da classe Edition de tamanho especificado com dados aleatórios.
    """

    books = []
    for i in range(number_of_editions):
        books.append(Edition(
            isbn=fake.isbn13().replace('-', ''),
            price=random.randint(50, 330),
            year=fake.year(), 
            stock_quantity=random.randint(1, 10001),
            num_pages=random.randint(30, 1500),
            publisher_code=publisher_code,
            book_code=book_code
         ))
    
    return books
