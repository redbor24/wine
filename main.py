from http.server import HTTPServer, SimpleHTTPRequestHandler

import configargparse
from jinja2 import Environment, FileSystemLoader, select_autoescape

import data
from tools import get_company_age_caption


def main():
    arg_parser = configargparse.ArgParser()
    arg_parser.add_argument(
        '-df',
        required=True,
        type=str,
        help='List of wines to load in Excel format.'
             ' See "wineslist_template.xlsx" for example')
    args = arg_parser.parse_args()
    wines_filepath = args.df

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        company_age_caption=get_company_age_caption(),
        wines=data.load_wines(wines_filepath)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    print('Кликните http://127.0.0.1:8000 для просмотра')
    server.serve_forever()


if __name__ == '__main__':
    main()
