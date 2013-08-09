#!/usr/bin/env python

from setuptools import setup
 
setup (
    name = "tt",
    version = "0.1",
    description="(tt) - time tracker",
    long_description="lightweight command line tool to track time for projects",
    author="Antonino Catinello",
    author_email="ac@antoo.org",
    url="http://antonino.catinello.eu",
    license = "MIT",
    packages = ['tt'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ], 
    download_url = "https://github.com/catinello/tt.git",
    zip_safe = True,
    entry_points = {
        'console_scripts': ['tt = tt.core:main']
    }
)