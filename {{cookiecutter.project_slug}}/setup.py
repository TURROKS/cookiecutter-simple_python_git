#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='{{cookiecutter.project_name}}',
      version='{{cookiecutter.project_version}}',
      description='{{cookiecutter.project_description}}',
      author='{{cookiecutter.project_author}}',
      author_email='{{cookiecutter.author_email}}',
      url='',
      packages=find_packages(include=['scripts']),
      entry_points={
        'console_scripts': []
      },
      install_requires=[],
      )
