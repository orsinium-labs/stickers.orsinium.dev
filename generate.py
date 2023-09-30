import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader('.'))
with open('info.yml') as stream:
    items: list = yaml.safe_load(stream)
template = env.get_template('index.html.j2')

# public_dir = Path('public')
items.sort(key=lambda item: item['date'], reverse=True)
with Path('index.html').open('w') as stream:
    html = template.render(items=items)
    stream.write(html)
