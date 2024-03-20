from database import Database
from data_generator import generate_nacionalities, generate_languages

if __name__ == '__main__':
    db = Database()
    
    nacionalities = generate_nacionalities()
    db.insert_nacionalities(nacionalities)

    