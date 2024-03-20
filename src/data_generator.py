import pandas as pd
import os
from entities import Nationality, Language

_PARENT_DIR = os.path.dirname(os.path.realpath(__file__))
_DATA_PATH = os.path.join(_PARENT_DIR, '..', 'data')

def generate_languages():
    data = pd.read_csv(os.path.join(_DATA_PATH, 'languages.csv'), index_col=None)
    data = data[['ISO 639-2 Code', 'English name of Language']]
    data['English name of Language'] = data['English name of Language'].apply(lambda x: x.split(';')[0])

    languages = [Language(row['ISO 639-2 Code'], row['English name of Language']) for _, row in data.iterrows()]

    return languages

def generate_nacionalities():
    data = pd.read_csv(os.path.join(_DATA_PATH, 'countries.csv'), keep_default_na=False)
    data = data[['alpha-2', 'name']]

    nacionalities = [Nationality(row['alpha-2'], row['name']) for _, row in data.iterrows()]

    return nacionalities
