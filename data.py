import pandas
from pprint import pprint


def load_excel(filename):
    excel_data_df = pandas.read_excel(filename, sheet_name='Лист1')
    return excel_data_df.to_dict(orient='records')


if __name__ == '__main__':
    excel_data = pandas.read_excel(
        'wine2.xlsx',
        sheet_name='Лист1',
        na_values='nan',
        keep_default_na=False
    )
    excel_dict = excel_data.to_dict(orient='records')
    # print(excel_dict)
    print(pprint(excel_dict))
