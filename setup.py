from setuptools import setup, find_packages

setup(
    name='pkg_const',
    version='0.0.1',
    packages=find_packages(where='create_package'),
    scripts=['script/constructor']
)
