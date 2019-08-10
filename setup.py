try:
    from setuptools import setup:
except ImportError:
    from distutils.core import setup

config = {
 'description': ' DB tool',
 'author': 'Maytham Alherz',
 'url': '',
 'download_url': '.',
 'author_email': 'gmaytham@gmail.com',
 'version': '0.1',
 'install_requires': [],
 'name': 'Dbtools'
}

 setup(**config)
