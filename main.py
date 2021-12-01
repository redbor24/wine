from datetime import datetime
from dateutil.relativedelta import relativedelta
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


def plural_days(n):
    days = ['год', 'года', 'лет']

    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n) + ' ' + days[p]


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

company_founded = datetime(year=1920, month=1, day=1)
company_old = relativedelta(datetime.today(), company_founded).years

template = env.get_template('template.html')

rendered_page = template.render(
    company_old=plural_days(company_old)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()