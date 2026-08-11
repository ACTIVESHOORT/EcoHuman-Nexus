from setuptools import setup, find_packages

setup(
    name="ecohuman-nexus",
    version="0.2.1",
    author="EcoHuman Contributors",
    description="A modular Python framework for localized environmental resource allocation and emissions tracking.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ecohuman=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
