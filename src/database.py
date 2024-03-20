import os
from dotenv import load_dotenv
import mysql.connector as conector

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

    def insert_nacionalities(self, nacionalities) -> bool:
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
    
    def insert_languages(self, languages) -> bool:
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
    
    def insert_authors(self, authors):
        inserted_ids = []

        try:
            sql = 'INSERT INTO autor (nome, data_nascimento, nota_bibliografica, codigo_nacionalidade) VALUES (%s, %s, %s, %s)'
            
            with self.connection.cursor() as cursor:
                for author in authors:
                    data = (author.name, author.date_of_birth.strftime("%Y-%m-%d"), author.biographic_note, author.nationality_code)
                    cursor.execute(sql, data)
                    inserted_ids.append(cursor.lastrowid)
            
            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "autor": {error}')
            inserted_ids.clear()
        
        return inserted_ids
    
    def insert_publishers(self, publishers):
        inserted_ids = []

        try:
            sql = 'INSERT INTO editora (nome, telefone, endereco) VALUES (%s, %s, %s)'
            
            with self.connection.cursor() as cursor:
                for pub in publishers:
                    data = (pub.name, pub.phone, pub.address)
                    cursor.execute(sql, data)
                    inserted_ids.append(cursor.lastrowid)
            
            self.connection.commit()
        except Exception as error:
            print(f'Erro ao inserir dados na tabela "autor": {error}')
            inserted_ids.clear()

        return inserted_ids
