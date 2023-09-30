import subprocess
import yaml
from jinja2 import Environment, FileSystemLoader
from shutil import copytree
from pathlib import Path

env = Environment(loader=FileSystemLoader('.'))
with open('info.yml') as stream:
    items: list = yaml.safe_load(stream)
template = env.get_template('index.html.j2')

public_dir = Path('public')
public_dir.mkdir(exist_ok=True)
svg_dir = Path('svgs')
assert svg_dir.is_dir()
png_dir = public_dir / 'pngs'
png_dir.mkdir(exist_ok=True)

copytree(
    svg_dir,
    public_dir / 'svgs',
    dirs_exist_ok=True,
)
for svg_path in svg_dir.iterdir():
    png_path = png_dir / f'{svg_path.stem}.png'
    cmd = [
        'inkscape',
        '--export-filename', str(png_path),
        '--export-width', '600',
        str(svg_path),
    ]
    subprocess.run(cmd).check_returncode()

items.sort(key=lambda item: item['date'], reverse=True)
html = template.render(items=items)
(public_dir / 'index.html').write_text(html)
