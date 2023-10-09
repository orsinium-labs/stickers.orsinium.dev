import subprocess
from shutil import copytree
from pathlib import Path

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
