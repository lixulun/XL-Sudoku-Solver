from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sudokuless",
    version="1.0.2",
    packages=['sudokuless'],
    entry_points={
        "console_scripts": [
            "sudokuless = sudokuless.__main__:main"
        ]
    },
    include_package_data=True,
    test_suite="tests",

    author="Xulun Li",
    author_email="lixulun99@hotmail.com",
    description="A simple Sudoku solver",
    license="MIT",
    url="https://github.com/lixulun/sudokuless",
    long_description=long_description,
    long_description_content_type="text/markdown"
)