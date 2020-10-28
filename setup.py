from setuptools import setup, find_packages

classifiers = ['Programming Language" :: Python :: 3']

setup(
  name = 'pytrainapi',
  packages = ['pytrainapi'], 
  version = '2.1',
  description = 'A library for fetching train details from source to destination',
  author = 'Viraj Mane',
  author_email = 'virajmane@protonmail.com',
  license = 'GPLv2',
  url = 'https://github.com/virajmane/pytrainapi', 
  download_url = 'https://github.com/virajmane/pytrainapi', 
  keywords = ['train', 'railway', 'station', 'api', 'traininfo'], 
  install_requires=['bs4','requests'])
