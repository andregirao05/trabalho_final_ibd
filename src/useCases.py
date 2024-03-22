from database import Database

from data_generator import (
    generate_nacionalities, 
    generate_languages,
    generate_authors,
    generate_publishers,
    generate_books,
    generate_editions
)

from random import choice, randint

def insert_all_nacionalities_use_case(db: Database):
    """
        Para deixar o banco de dados supimpa, a livraria resolve cadastrar de uma vez todas 
        as nacionalidades possíveis.
    """

    nacionalities = generate_nacionalities()
    db.insert_all_nacionalities(nacionalities)

def insert_all_languages_use_case(db: Database):
    """
        Todos os idiomas disponíveis, reconhecidos pela ONU, são cadastrados no banco de dados
    """
    languages = generate_languages()
    db.insert_all_languages(languages)

def insert_authors_without_books_use_case(db: Database):
    """
        A livraria resolve cadastrar um autores muito conhecidos no seu banco de dados, 
        embora não possua nenhum livro do mesmo disponível para a venda.
    """
    authors = generate_authors()
    db.insert_all_authors(authors) 


def insert_publishers_without_editions_use_case(db: Database):
    """
        A livraria resolve cadastrar um autores muito conhecidos no seu banco de dados, 
        embora não possua nenhum livro do mesmo disponível para a venda.
    """
    publishers = generate_publishers()
    db.insert_all_publishers(publishers)


def insert_pulishers_authors_books_and_editions_use_case(db: Database):
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

def insert_only_editions_use_case(db: Database):
    """
        A livraria comprou de diferentes editoras várias edições de um livro de um autor já cadastrado.
    """
    random_publisher_codes = db.get_random_publisher_codes()
    random_books_codes = db.get_random_book_codes()

    for book_code in random_books_codes:
        publiser_code = choice(random_publisher_codes)
        new_editions = generate_editions(publisher_code=publiser_code, number_of_editions=randint(1, 5), book_code=book_code)
        db.insert_editions(new_editions)
