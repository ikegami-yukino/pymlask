# -*- coding: utf-8 -*-
from codecs import open
import os
import pkgutil
import re
from setuptools import setup

install_requires = [] if pkgutil.find_loader('MeCab') else ['mecab-python-windows']

with open(os.path.join('mlask', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='pymlask',
    packages=['mlask'],
    version=version,
    license='The BSD 3-Clause License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='Emotion analyzer for Japanese',
    author='Yukino Ikegami',
    author_email='yknikgm@gmail.com',
    url='https://github.com/ikegami-yukino/pymlask',
    keywords=['emotion analysis'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Text Processing :: Linguistic'
    ],
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read()),
    package_data={'mlask': ['emotemes/*.txt', 'emotions/*.txt']},
    install_requires=install_requires,
    tests_require=['nose'],
    test_suite='nose.collector'
)
