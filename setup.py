try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "Fiona Guoguo Lu's personal blog",
    'author': 'Fiona Guoguo Lu',
    'url': 'https://github.com/fionaguoguolu/flblog',
    'author_email': 'dev@fionalu.me',
    'version': '0.1',
    'install_requires': [
        'pytest',
        'ipdb',
        'flake8',
        ],
    'packages': ['FLBLOG'],
    'scripts': [],
    'name': 'flblog'
}

setup(**config)
