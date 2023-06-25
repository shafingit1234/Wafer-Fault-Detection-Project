from setuptools import find_packages, setup
# Required to use user created packages.
# to execute it use command python setup.py install
# before executing the setup.py file, when we will execute pip install command,
# we will not be able to find the user created package which in this case is src package
# After executing setup.py file, pip list will also show us src as a recognized package.
# This setup.py will also make sure that this package (src or user created package), will be present in my local environment which means in venv.

setup(
    name="src",
    version="0.0.1",
    author="shafin",
    author_email="shafinmohammed315@gmail.com",
    packages=find_packages(),
    install_requires = [],
)