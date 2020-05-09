#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ElmPy",
    version="0.2.0",
    author="Julian Theis",
    author_email="julian.theis@posteo.de",
    description="Simple Extreme Learning Machine implemented with NumPy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvytee/elmpy",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[
        'numpy'
    ],
    extras_require={
        'sklearn': ['scikit-learn'],
        'test': ['pytest']
    },
    python_requires='>=3.7'
)
