from collections import defaultdict

import pandas


def import_excel_datafile(filename):
    excel_data = pandas.read_excel(
        filename,
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False
    )
    wines = defaultdict(list)

    for wine in excel_data.to_dict(orient='records'):
        wines[wine['Категория']].append(wine)

    return wines


def my_key(wine):
    return wine['Категория']
