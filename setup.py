import pathlib
from setuptools import setup, find_packages


base_packages = [
    "scikit-learn>=1.0.0",
    "vaderSentiment==3.3.2",
    "textblob==0.17.1",
    "pandas>=1.3.3",
]

docs_packages = [
    "mkdocs==1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings==0.8.0",
    "mktestdocs==0.1.2",
]

test_packages = [
    "interrogate>=1.5.0",
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "pre-commit>=2.2.0",
    "whatlies==0.6.4",
]

all_packages = base_packages
dev_packages = all_packages + docs_packages + test_packages


setup(
    name="sentimany",
    version="0.1.0",
    author="Vincent D. Warmerdam",
    packages=find_packages(exclude=["notebooks", "docs"]),
    description="Just a bunch of imperfect sentiment models.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/koaning/sentimany/",
        "Issue Tracker": "https://github.com/koaning/sentimany/issues",
    },
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    license_files=("LICENSE",),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
