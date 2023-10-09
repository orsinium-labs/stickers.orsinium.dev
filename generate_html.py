import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader('.'))
with open('info.yml') as stream:
    items: list = yaml.safe_load(stream)
template = env.get_template('index.html.j2')

public_dir = Path('public')
public_dir.mkdir(exist_ok=True)
items.sort(key=lambda item: item['date'], reverse=True)
html = template.render(items=items)
(public_dir / 'index.html').write_text(html)
