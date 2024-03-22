import os
from dotenv import load_dotenv
import mysql.connector as conector

from entities import Book

load_dotenv()


class Database:
    """ Classe que conecta ao banco de dados e executa manipulções """
    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = conector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.disconnect()

    def insert_all_nacionalities(self, nacionalities) -> bool:
        results = True

        try:
            data = [(nacionality.code, nacionality.name) for nacionality in nacionalities]
            sql = 'INSERT INTO nacionalidade (codigo, nome) VALUES (%s, %s)'

            with self.connection.cursor() as cursor:
                cursor.executemany(sql, data)

            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "nacionalidade": {error}')
            results = False
        
        return results
    
    def insert_all_languages(self, languages) -> bool:
        results = True

        try:
            data = [(language.code, language.name) for language in languages]
            sql = 'INSERT INTO idioma (codigo, nome) VALUES (%s, %s)'

            with self.connection.cursor() as cursor:
                cursor.executemany(sql, data)
            
            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "idioma": {error}')
            results = False

        return results
    
    def insert_all_authors(self, authors):
        inserted = False

        try:
            sql = 'INSERT INTO autor (nome, data_nascimento, nota_bibliografica, codigo_nacionalidade) VALUES (%s, %s, %s, %s)'
            
            with self.connection.cursor() as cursor:
                data = [(author.name, author.date_of_birth.strftime("%Y-%m-%d"), author.biographic_note, author.nationality_code) for author in authors]
                cursor.executemany(sql, data)

            self.connection.commit()
            inserted = True
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "autor": {error}')
        
        return inserted
    
    def insert_author(self, author):
        inserted_id = None

        try:
            sql = 'INSERT INTO autor (nome, data_nascimento, nota_bibliografica, codigo_nacionalidade) VALUES (%s, %s, %s, %s)'
            
            with self.connection.cursor() as cursor:               
                data = (author.name, author.date_of_birth.strftime("%Y-%m-%d"), author.biographic_note, author.nationality_code)
                cursor.execute(sql, data)
                inserted_id = cursor.lastrowid
            
            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "autor": {error}')
        
        return inserted_id
    
    def insert_all_publishers(self, publishers):
        inserted = False

        try:
            sql = 'INSERT INTO editora (nome, telefone, endereco) VALUES (%s, %s, %s)'
            
            with self.connection.cursor() as cursor:
                data = [(pub.name, pub.phone, pub.address) for pub in publishers]
                cursor.executemany(sql, data)
            
            self.connection.commit()
            inserted = True
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "editora": {error}')

        return inserted
    
    def insert_publisher(self, publisher):
        inserted_id = None

        try:
            sql = 'INSERT INTO editora (nome, telefone, endereco) VALUES (%s, %s, %s)'
            
            with self.connection.cursor() as cursor:
                data = (publisher.name, publisher.phone, publisher.address)
                cursor.execute(sql, data)
                inserted_id = cursor.lastrowid

            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "editora": {error}')

        return inserted_id
    
    def insert_book_and_editions(self, book, editions):
        inserted = False

        try: 
            with self.connection.cursor() as cursor:
                # inserir livro
                insert_book_sql = 'INSERT INTO livro (titulo, ano, codigo_idioma) VALUES (%s, %s, %s)'
                book_data = (book.title, book.year, book.language_code)
                cursor.execute(insert_book_sql, book_data)
                book.code = cursor.lastrowid

                # inserir relacionamento escreve
                insert_write_sql = 'INSERT INTO escreve (codigo_autor, codigo_livro) VALUES (%s, %s)'
                write_data = (book.author_code, book.code)
                cursor.execute(insert_write_sql, write_data)

                # inserir edições
                insert_edition_sql = 'INSERT INTO edicao (isbn, ano, numero_paginas, valor, quantidade_estoque, codigo_livro, codigo_editora) VALUES (%s, %s, %s, %s, %s, %s, %s)'

                for edition in editions:
                    edition.book_code = book.code
                    edition_data = (edition.isbn, edition.year, edition.num_pages, edition.price, edition.stock_quantity, edition.book_code, edition.publisher_code)
                    cursor.execute(insert_edition_sql, edition_data)
                    edition.code = cursor.lastrowid

            self.connection.commit()
            inserted = True
        except Exception as error:
            print(f'Erro ao inserir dados de livros e edições": {error}')

        return inserted
    
