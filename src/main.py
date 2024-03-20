"""
    Arquivo principal onde o DB é populado
"""

from database import Database
from data_generator import (
    generate_nacionalities, 
    generate_languages,
    generate_authors_without_books,
    generate_publishers
)

if __name__ == '__main__':
    db = Database()
    
    #adiciona nacionalidades
    nacionalities = generate_nacionalities()
    db.insert_nacionalities(nacionalities)

    #adiciona idiomas
    languages = generate_languages()
    db.insert_languages(languages)

    #adiciona os autores, porém sem seus livros
    authors_withour_books = generate_authors_without_books()
    author_codes = db.insert_authors(authors_withour_books) 

    #adiciona editoras, porém sem edições
    publishers = generate_publishers()
    publisher_codes = db.insert_publishers(publishers)