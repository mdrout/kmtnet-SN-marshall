from setuptools import setup

setup(name='kmtshi',
      author=['Maria Drout', 'Curtis McCully'],
      author_email=['maria.drout@dunlap.utoronto.ca', 'cmccully@lco.global'],
      version=0.1,
      packages=['kmtshi'],
      setup_requires=[],
      install_requires=['numpy', 'astropy', 'django','pillow','bokeh','astroquery'],
      tests_require=[]
      )
