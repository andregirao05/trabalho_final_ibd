import os
from dotenv import load_dotenv
import mysql.connector as conector

load_dotenv()


class Database:
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
        cursor = None

        try:
            data = [(nacionality.code, nacionality.name) for nacionality in nacionalities]
            sql = 'INSERT INTO nacionalidade (codigo, nome) VALUES (%s, %s)'

            cursor = self.connection.cursor()
            cursor.executemany(sql, data)
            self.connection.commit()
        except conector.Error as erro:
            print(f'Erro ao inserir dados na tabela "nacionalidade": {erro}')
            results = False
        finally:
            if cursor:
                cursor.close()

        return results
    
    def insert_languages(self, languages) -> bool:
        results = True
        cursor = None

        try:
            data = [(language.code, language.name) for language in languages]
            sql = 'INSERT INTO idioma (codigo, nome) VALUES (%s, %s)'

            cursor = self.connection.cursor()
            cursor.executemany(sql, data)
            self.connection.commit()
        except conector.Error as erro:
            print(f'Erro ao inserir dados na tabela "idioma": {erro}')
            results = False
        finally:
            if cursor:
                cursor.close()

        return results
    
    def insert_authors(self, authors):
        results = True
        cursor = None

        try:
            data = [(author.name, author.date_of_birth.strftime("%Y-%m-%d"), author.biographic_note, author.nationality_code) for author in authors]
            sql = 'INSERT INTO autor (nome, data_nascimento, nota_bibliografica, codigo_nacionalidade) VALUES (%s, %s, %s, %s)'

            cursor = self.connection.cursor()
            cursor.executemany(sql, data)
            self.connection.commit()
        except conector.Error as erro:
            print(f'Erro ao inserir dados na tabela "autor": {erro}')
            results = False
        finally:
            if cursor:
                cursor.close()

        return results
    
    def insert_publishers(self, publishers):
        results = True
        cursor = None

        try:
            data = [(pub.name, pub.phone, pub.address) for pub in publishers]
            sql = 'INSERT INTO editora (nome, telefone, endereco) VALUES (%s, %s, %s)'

            cursor = self.connection.cursor()
            cursor.executemany(sql, data)
            self.connection.commit()
        except conector.Error as erro:
            print(f'Erro ao inserir dados na tabela "autor": {erro}')
            results = False
        finally:
            if cursor:
                cursor.close()

        return results
