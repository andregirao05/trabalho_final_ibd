from database import Database
from data_generator import (
    generate_nacionalities, 
    generate_languages,
    generate_authors_without_books,
    generate_publishers
)

if __name__ == '__main__':
    db = Database()
    
    nacionalities = generate_nacionalities()
    db.insert_nacionalities(nacionalities)

    languages = generate_languages()
    db.insert_languages(languages)

    authors_withour_books = generate_authors_without_books()
    db.insert_authors(authors_withour_books) 

    publishers = generate_publishers()
    db.insert_publishers(publishers)
