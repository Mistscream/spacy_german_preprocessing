import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy_german_preprocess",
    version="0.0.1",
    author="Sebastian Jüngling",
    author_email="author@example.com",
    description="A small package for preprocessing german text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mistscream/spacy_german_preprocessing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)