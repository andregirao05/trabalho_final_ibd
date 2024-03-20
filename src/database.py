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