from setuptools import setup, find_packages
import sys, os

version = "0.1"

setup(
    name='ckanext-parkinsons',
    version=version,
    description="Parkison's UK Research Data",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='James Gardner',
    author_email='james@3aims.com',
    url='',
    license='Commercial',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.parkinsons'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    myplugin=ckanext.parkinsons.plugin:ParkinsonsPlugin
    """,
)
