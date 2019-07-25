try:
    from setuptools import setup:
except ImportError:
    from distutils.core import setup

config = {
 'description': 'First go on making a DB',
 'author': 'Maytham Alherz',
 'url': '',
 'download_url': '.',
 'author_email': 'My email.',
 'version': '0.1',
 'install_requires': [],
 'packages': [],
 'scripts': [],
 'name': 'DB'
}

 setup(**config)
