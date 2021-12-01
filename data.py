import collections
import pandas
from pprint import pprint


def load_excel(filename):
    excel_data = pandas.read_excel(
        filename,
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False
    )
    return get_restructed_excel_data(excel_data.to_dict(orient='records'))


def get_restructed_excel_data(excel_data):
    restructed_excel_data = collections.defaultdict(list)

    for item_n, item in enumerate(excel_data):
        wine = {
            'Категория': item['Категория'],
            'Картинка': item['Картинка'],
            'Название': item['Название'],
            'Сорт': item['Сорт'],
            'Цена': item['Цена'],
        }
        restructed_excel_data[item['Категория']].append(wine)

    return restructed_excel_data


if __name__ == '__main__':
    pprint(load_excel('wine2.xlsx'))

