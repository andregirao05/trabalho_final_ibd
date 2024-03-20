from database import Database

if __name__ == '__main__':
    db = Database()
    print(db.connection.is_connected())