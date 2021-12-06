from http.server import HTTPServer, SimpleHTTPRequestHandler

import configargparse
from jinja2 import Environment, FileSystemLoader, select_autoescape

import data
from tools import get_company_age

p = configargparse.ArgParser()
p.add_argument('-df', required=True, type=str,
               help='Excel-list of wines to load')
args = p.parse_args()
wines_excel_file = args.df

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    company_age=get_company_age(),
    wines=data.load_excel(wines_excel_file)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
