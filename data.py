import pandas


def load_excel(filename):
    excel_data_df = pandas.read_excel(filename, sheet_name='Лист1')
    return excel_data_df.to_dict(orient='records')
