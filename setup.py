from setuptools import setup, find_packages

setup(
    name="stockprice-cli",
    packages=find_packages(exclude=["tests"]),
    email="thomasmcinally@hotmail.com",
    author="Thomas Mcinally",
    url="https://github.com/Thomas-mcinally/stockplot",
    long_description_content_type="text/markdown",
    install_requires=["yfinance", "pandas"],
    version="1.0.1",
    entry_points={"console_scripts": ["stockprice = stockprice.main:main"]},
)
