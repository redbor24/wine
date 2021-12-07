import time

WINE_COMPANY_BIRTH_YEAR = 1920


def get_year_plural_name(year):
    year_plural_names = ['год', 'года', 'лет']

    if year % 10 == 1 and year % 100 != 11:
        year_name_index = 0
    elif 2 <= year % 10 <= 4 and (year % 100 < 10 or year % 100 >= 20):
        year_name_index = 1
    else:
        year_name_index = 2

    return str(year) + ' ' + year_plural_names[year_name_index]


def get_company_age_caption():
    current_year = int(time.strftime('%Y', time.localtime()))
    return get_year_plural_name(current_year - WINE_COMPANY_BIRTH_YEAR)
