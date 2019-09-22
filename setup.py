from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spack-detect',  # Required
    version='0.0.1',  # Required
    description='A program that detects system-provided Spack packages',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='Matthieu Dorier',  # Optional
    author_email='mdorier@anl.gov',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={  # Optional
        'console_scripts': [
            'spack-detect=spackdetect:main',
        ],
    },
)
