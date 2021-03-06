from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description =f.read()

setup(
    name = 'pgpackup',
    version = '0.1.0',
    author = 'Serik Tulegenov',
    author_email = 'tulegenoff.s@gmail.com',
    description = 'A utility for backing up PostgreSql databases',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/serik-tulegenov/pgbackup',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['boto3'],
    entry_points={
        'console_scripts': ['pgbackup = pgbackup.cli:main', ], }
    )
