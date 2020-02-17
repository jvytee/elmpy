#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ElmPy",
    version="0.0.1",
    author="jvytee",
    author_email="jvytee@posteo.org",
    description="Simple Extreme Learning Machine implemented with NumPy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvytee/pyelm",
    packages=find_packages(),
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
        'sklearn': ['scikit-learn']
    },
    python_requires='>=3.7'
)
