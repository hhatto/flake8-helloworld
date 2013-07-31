# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_helloworld.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

setup(
    name='flake8-helloworld',
    version=get_version(),
    description="Hello flake8 plugin",
    long_description="example of flake8 plugin",
    keywords='flake8',
    author='Hideo Hattori',
    author_email='hhatto.jp@gmail.com',
    url='https://github.com/hhatto/flake8-helloworld',
    license='MIT',
    py_modules=['flake8_helloworld'],
    install_requires=['flake8>=2.0'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'HW01 = flake8_helloworld:check_helloworld',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
