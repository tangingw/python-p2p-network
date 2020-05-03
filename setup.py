import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="p2pnet-macsnoeren",
    version="0.0.1",
    author="Maurice Snoeren",
    author_email="macsnoeren@gmail.com",
    description="Python decentralized peer-to-peer network application implementation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/macsnoeren/python-p2p-network",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU 3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)