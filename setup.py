from setuptools import setup, find_packages

setup(
    name="datanix",
    version="0.4",
    packages=find_packages(),
    install_requires=["pandas", "matplotlib"],
    author="Chandravardhan",
    description="A smart data cleaning package for Python!",
)