from distutils.core import setup
setup(
  name = 'logdna',
  packages = ['logdna'],
  version = '1.0.3',
  description = 'A python package for sending logs to LogDNA',
  author = 'Answerbook Inc.',
  author_email = 'help@logdna.com',
  url = 'https://github.com/logdna/python',
  download_url = 'https://github.com/logdna/python/tarball/1.0.3',
  keywords = ['logdna', 'logging', 'logs', 'python', 'logdna.com', 'logger'],
  install_requires=[
    'requests',
  ],
  classifiers = [],
)
