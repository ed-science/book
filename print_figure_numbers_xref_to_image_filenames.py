#!/usr/bin/env python
from pathlib import Path
import re

for path in sorted(Path(__file__).absolute().parent.glob('*.asciidoc')):
    images = re.findall(r'::images/(\w+\.png)', path.read_text())
    if not images:
        continue
    chapter_no = re.search(r'chapter_(\d\d)', str(path))
    chapter_no = str(int(chapter_no[1])) if chapter_no else '??'
    print(path.name)
    for ix, image in enumerate(images):
        print(f'  Figure {chapter_no}.{ix+1}: {image}')
