import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentence-url",
    version="0.0.1",
    author="Jab",
    description="Generates readable URLs like Twitch's clips",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jabbey92/sentence-url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
