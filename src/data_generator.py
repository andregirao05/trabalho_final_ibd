import pandas as pd
import os

_PARENT_DIR = os.path.dirname(os.path.realpath(__file__))
_DATA_PATH = os.path.join(_PARENT_DIR, '..', 'data')

def get_language_data():
    languages = pd.read_csv(os.path.join(_DATA_PATH, 'languages.csv'), index_col=None)
    languages = languages[['ISO 639-2 Code', 'English name of Language']]
    
    languages['English name of Language'] = languages['English name of Language'].apply(lambda x: x.split(';')[0])
    
    languages = languages.rename(columns={'ISO 639-2 Code': 'code', 'English name of Language': 'name'})

    return languages

def get_country_data():
    countries = pd.read_csv(os.path.join(_DATA_PATH, 'countries.csv'))
    countries = countries[['alpha-3', 'name']]

    countries = countries.rename(columns={'alpha-3': 'code'})

    return countries

