import os
from setuptools import find_packages, setup
from database import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'Django',
    'django-jet',
    'pytz',
    'python-dotenv',
    'psycopg2-binary',
    'djangorestframework',
    'django-filter',
    'django_extensions',
    'Markdown',
    'coreapi',
    'Pygments',
    'django-webpack-loader',
    'djangorestframework-jwt',
    'raven',
    'dejavu-base',
]

tests_require = [
    'coverage',
    'flake8',
]

extras_require = {
    'dev': [
        'bumpr',
        'factory_boy',
    ] + tests_require,
}

setup(
    name='django-calidae-database',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='database research for master thesis',
    url='https://bitbucket.org/calidae/database',
    author='Calidae',
    author_email='dev@calidae.com',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
)
