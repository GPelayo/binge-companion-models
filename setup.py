#!/usr/bin/env python

from setuptools import setup

setup(name='Binge Companion Models',
      version='0.1.2',
      description='Model Objects for Binge Companion',
      author='Geryl Pelayo',
      author_email='hi@gerylpelayo.com',
      packages=['binge_models'],
      install_requires=["sqlalchemy>=1.4.39",
                        "SQLAlchemy-serializer>=1.4.1"],
      )
