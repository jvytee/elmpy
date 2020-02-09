#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Skelm",
    version="0.0.1",
    author="jvytee",
    author_email="jvytee@posteo.org",
    description="Simple Extreme Learning Machine for scikit-learn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvytee/skelm",
    packages=find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires='>=3.7'
)
