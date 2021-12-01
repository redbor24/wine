from datetime import datetime
from dateutil.relativedelta import relativedelta
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import tools
import data

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

company_founded = datetime(year=1920, month=1, day=1)
company_old = relativedelta(datetime.today(), company_founded).years

template = env.get_template('template.html')

rendered_page = template.render(
    company_old=tools.plural_days(company_old),
    wines=data.load_excel('wine.xlsx')
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()