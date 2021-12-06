from datetime import datetime

from dateutil.relativedelta import relativedelta

WINE_COMPANY_BIRTH_YEAR = 1920


def get_year_plural(year):
    year_plural_names = ['год', 'года', 'лет']

    if year % 10 == 1 and year % 100 != 11:
        p = 0
    elif 2 <= year % 10 <= 4 and (year % 100 < 10 or year % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(year) + ' ' + year_plural_names[p]


def get_company_age():
    return get_year_plural(relativedelta(
        datetime.today(),
        datetime(year=WINE_COMPANY_BIRTH_YEAR, month=1, day=1)).years)
