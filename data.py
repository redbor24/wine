from collections import defaultdict
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
    restructed_excel_data = defaultdict(list)

    for item_n, item in enumerate(excel_data):
        wine = {
            'start_category': False,
            'stop_category': False,
            'Категория': item['Категория'],
            'Картинка': item['Картинка'],
            'Название': item['Название'],
            'Сорт': item['Сорт'],
            'Цена': item['Цена'],
        }
        restructed_excel_data[item['Категория']].append(wine)

    result = []
    category = ''
    for cat in restructed_excel_data.items():
        wine_count = len(cat[1])
        for wine_n, wine in enumerate(cat[1], start=1):
            wine['start_category'] = (category != wine['Категория'])
            wine['stop_category'] = (wine_count == wine_n)

            if category != wine['Категория']:
                category = wine['Категория']

            result.append(wine)

    return result


if __name__ == '__main__':
    excel_data = load_excel('wine2_1.xlsx')
    # print(type(excel_data))
    pprint(excel_data)
    # print(len(excel_data))
    #
