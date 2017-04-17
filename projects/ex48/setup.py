try: 
	from setuptools import setup
except ImportError: 
	from distutils.core import setup
	
config = {
	'description': 'My Project',
    'author': 'michael vincerra',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'michael.vincerra@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon.py', 'parser.py'],
    'scripts': [],
}

setup(**config)