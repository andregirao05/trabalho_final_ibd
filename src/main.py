"""
    Arquivo principal onde o DB é populado
"""

from database import Database
from useCases import *


if __name__ == '__main__':
    print("Iniciando...")

    db = Database()

    print("Executando casos de uso:\n")

    insert_all_nacionalities_use_case(db)
    insert_all_languages_use_case(db)
    insert_authors_without_books_use_case(db)
    insert_publishers_without_editions_use_case(db)
    insert_pulishers_authors_books_and_editions_use_case(db)
    insert_only_editions_use_case(db)

    print("\nProcesso finalizado!")