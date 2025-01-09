from setuptools import setup, find_packages

setup(
    name="maths_tables_py",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tables=math_tables_py.bin.start_tables:main",
        ],
    },
)
