from collections import defaultdict

import pandas


def load_wines(filename):
    wines = pandas.read_excel(
        filename,
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False
    ).to_dict(orient='records')

    wines_by_category = defaultdict(list)
    for wine in wines:
        wines_by_category[wine['Категория']].append(wine)

    return wines_by_category


def my_key(wine):
    return wine['Категория']
