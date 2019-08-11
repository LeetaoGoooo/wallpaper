# -*- coding:utf-8 -*-

import os
import sys
from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


# for publish shortcut
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['wallpaper']

about = {}
with open(os.path.join(here, 'wallpaper', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name = about['__title__'],
    version = about['__version__'],
    description=about['__description__'],
    url = 'https://www.leetao94.cn',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=packages,
    package_data={'': ['LICENSE'], 'wallpaper': ['wallpaper/macos-wallpaper','wallpaper/win-wallpaper.exe']},
    include_package_data=True,
    package_dir={'wallpaper': 'wallpaper'},
    python_requires=">=3.0.*",
    license=about['__license__'],
    zip_safe=False
)