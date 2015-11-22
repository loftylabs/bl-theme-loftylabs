from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst')) as f:
    long_description = f.read()

setup(
    name="bl-theme-loftylabs",
    version='0.0.1.1',

    descripition='Baseline theme for the lofty labs website',
    long_description=long_description,

    url='https://github.com/loftylabs/bl-theme-loftylabs',

    author='Lofty Labs',
    author_email='casey@hirelofty.com',

    license = 'MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        
        # TODO: Test with tox and indicate other supported versions here
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='cms blog blogging platform website builder',

    packages=find_packages(exclude=['tests*']),
    package_data={'bl-theme-loftylabs': ['static*', 'templates*']},
    install_requires=[]
)
