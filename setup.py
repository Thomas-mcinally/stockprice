from setuptools import setup, find_packages

setup(
    dependency_links=[],
    name="stockprice-cli",
    packages=find_packages(exclude=["tests"]),
    email="thomasmcinally@hotmail.com",
    author="Thomas Mcinally",
    url="https://github.com/Thomas-mcinally/stockprice",
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    install_requires=[
        "certifi==2022.12.7; python_version >= '3.6'",
        "charset-normalizer==3.1.0; python_full_version >= '3.7.0'",
        "idna==3.4; python_version >= '3.5'",
        "requests==2.28.2",
        "urllib3==1.26.14; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
    ],
    version="2.1.1",
    entry_points={"console_scripts": ["stockprice = stockprice.main:main"]},
)
