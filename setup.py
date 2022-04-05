#!/usr/bin/env python3

from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="netprot",
    version="0.1.1",
    description="A system-indipendent network protocol manipulation and evaluation library.",
    author="Federico Olivieri",
    author_email="lvrfrc87@mail.com",
    url="https://github.com/lvrfrc87/netprot",
    packages=["netprot"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
