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
    restructed_excel_data = {}

    for item_n, item in enumerate(excel_data):
        wine = {
            'Картинка': item['Картинка'],
            'Название': item['Название'],
            'Сорт': item['Сорт'],
            'Цена': item['Цена'],
        }
        if restructed_excel_data.get(item['Категория']):
            restructed_excel_data[item['Категория']].append(wine)
        else:
            restructed_excel_data[item['Категория']] = [wine]

    return restructed_excel_data


if __name__ == '__main__':
    excel_dict = load_excel2('wine2.xlsx')
    # print(pprint(excel_dict))
    print(pprint(get_restructed_excel_data(excel_dict)))
