# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pyse/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='pyse',
    version=version,
    url='https://github.com/defnngj/pyse/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='WebUI automation testing framework based on Selenium and Nose ',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Selenium>=2.53.0',
        'nose>=1.3.7',
        'nose-html-reporting>=0.2.3',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Ubuntu',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries ::Testing'
    ],
    entry_points='''
        [console_scripts]
        pyse=pyse.Pyse:main
    '''
)