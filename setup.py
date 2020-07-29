from setuptools import setup

with open("README") as f:
    long_description = f.read()

setup(
    name="csv_converter",
    version="1.1.0",
    description="Converts a list of hotels from a csv into a json wich is \
        readable by the conversion tool",
    license="MIT",
    long_description=long_description,
    author="Maximillian Rampulla",
    author_email="maxrampulla@gmail.com",
    py_modules=["csv_converter"]
)
