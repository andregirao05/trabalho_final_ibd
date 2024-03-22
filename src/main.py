"""
    Arquivo principal onde o DB é populado
"""

from database import Database
from data_generator import (
    generate_nacionalities, 
    generate_languages,
    generate_authors,
    generate_publishers,
    generate_books,
    generate_editions
)

from random import shuffle, randint

def useCase1(db):
    """
        Para deixar o banco de dados supimpa, a livraria resolve cadastrar de uma vez todas 
        as nacionalidades possíveis.
    """

    nacionalities = generate_nacionalities()
    db.insert_all_nacionalities(nacionalities)

def useCase2(db):
    """
        Todos os idiomas disponíveis, reconhecidos pela ONU, são cadastrados no banco de dados
    """
    languages = generate_languages()
    db.insert_all_languages(languages)

def useCase3(db):
    """
        A livraria resolve cadastrar um autores muito conhecidos no seu banco de dados, 
        embora não possua nenhum livro do mesmo disponível para a venda.
    """
    authors = generate_authors()
    author_codes = db.insert_all_authors(authors) 

    return author_codes

def useCase4(db):
    """
        A livraria resolve cadastrar um autores muito conhecidos no seu banco de dados, 
        embora não possua nenhum livro do mesmo disponível para a venda.
    """
    publishers = generate_publishers()
    publisher_codes = db.insert_all_publishers(publishers)

    return publisher_codes

def useCase5(db):
    """
        A livraria fechou contrato com uma editora já cadastrada e recebeu toda a obras de 
        diversos autores. Alguns autores podem já estarem cadastrados.
    """
    publishers = generate_publishers(number_of_publishers=50)

    for publisher in publishers:
        publisher.code = db.insert_publisher(publisher)

        authors = generate_authors(number_of_authors=randint(2, 5))

        for author in authors:
            author.code = db.insert_author(author)

            books = generate_books(number_of_books=randint(4, 10), author_code=author.code)

            for book in books:
                editions = generate_editions(number_of_editions= randint(3, 10), publisher_code=publisher.code)
                db.insert_book_and_editions(book, editions)

def useCase6(db):
    """
        A livraria comprou várias edições de um livro de um autor já cadastrado, porém as edições 
        podem ser de editoras diferentes ou ainda não disponíveis no banco. Os dados das editoras 
        são passados também.
    """
    pass

if __name__ == '__main__':
    db = Database()

    useCase1(db)

    useCase2(db)

    useCase3(db)  

    useCase4(db)

    useCase5(db)
