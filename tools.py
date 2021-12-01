from datetime import datetime
from dateutil.relativedelta import relativedelta


def plural_days(n):
    days = ['год', 'года', 'лет']

    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n) + ' ' + days[p]


def get_company_age_plural():
    company_founded = datetime(year=1920, month=1, day=1)
    return relativedelta(datetime.today(), company_founded).years

