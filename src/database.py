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
            cursor.close()

        return results
    
    def insert_languages(self, languages) -> bool:
        results = True

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
            cursor.close()

        return results