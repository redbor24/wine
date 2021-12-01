import collections
import pandas
from pprint import pprint


def load_excel(filename):
    excel_data_df = pandas.read_excel(filename, sheet_name='Лист1')
    return excel_data_df.to_dict(orient='records')


def load_excel2(filename):
    excel_data = pandas.read_excel(
        filename,
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False
    )
    return excel_data.to_dict(orient='records')


def get_restructed_excel_data(excel_data):
    restructed_excel_data = collections.defaultdict(list)

    for item_n, item in enumerate(excel_data):
        wine = {
            'Картинка': item['Картинка'],
            'Название': item['Название'],
            'Сорт': item['Сорт'],
            'Цена': item['Цена'],
        }
        restructed_excel_data[item['Категория']].append(wine)

    return restructed_excel_data


if __name__ == '__main__':
    # dict_of_lists = collections.defaultdict(list)
    # print(dict_of_lists)
    # dict_of_lists['a'].append({'a': 'a', 'x': 1})
    # dict_of_lists['a'].append({'a': 'a2', 'x': 2})
    # dict_of_lists['b'].append({'b': 'b1', 'x': 3})
    # pprint(dict_of_lists)
    # exit()

    excel_dict = load_excel2('wine2.xlsx')
    pprint(get_restructed_excel_data(excel_dict))

