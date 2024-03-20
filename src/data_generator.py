import pandas as pd
import os
from entities import (
    Nationality, 
    Language,
    Author,
    Publisher
)

from faker import Faker
import random
from datetime import datetime

_PARENT_DIR = os.path.dirname(os.path.realpath(__file__))
_DATA_PATH = os.path.join(_PARENT_DIR, '..', 'data')

fake = Faker('pt-BR')

def generate_languages():
    data = pd.read_csv(os.path.join(_DATA_PATH, 'languages.csv'), index_col=None)
    data = data[['ISO 639-2 Code', 'English name of Language']]
    data['English name of Language'] = data['English name of Language'].apply(lambda x: x.split(';')[0])
    data['ISO 639-2 Code'] = data['ISO 639-2 Code'].apply(lambda x: x.split('-')[0])

    languages = [Language(row['ISO 639-2 Code'], row['English name of Language']) for _, row in data.iterrows()]

    return languages

def generate_nacionalities():
    data = pd.read_csv(os.path.join(_DATA_PATH, 'countries.csv'), keep_default_na=False)
    data = data[['alpha-2', 'name']]

    nacionalities = [Nationality(row['alpha-2'], row['name']) for _, row in data.iterrows()]

    return nacionalities

def generate_authors_without_books(number_of_authors = 20):
    authors = []

    for i in range(number_of_authors):
        authors.append(Author(
            name=fake.name(),
            date_of_birth=datetime.strptime(fake.date(), "%Y-%m-%d"),
            biographic_note=fake.sentence(),
            nationality_code=fake.country_code()
        ))

    return authors

def generate_publishers(number_of_publishers = 20):
    publishers = []

    for i in range(number_of_publishers):
        publishers.append(Publisher(
            name=fake.company(),
            phone=''.join(char for char in fake.phone_number() if char.isdigit() or char.isspace()),
            address=fake.address()
        ))

    return publishers