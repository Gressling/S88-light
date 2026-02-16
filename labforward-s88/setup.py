from setuptools import setup, find_packages

setup(
    name="labforward-s88-light",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas",
        "python-dotenv",
    ],
    extras_require={
        "validation": [
            "lxml",
            "jsonschema",
        ],
    },
    author="Peter Dinh & Alexander Reiling",
    author_email="peter.dinh@bayer.com",
    description="Python library for Laboperator API integration and S88-light recipe generation (XML & JSON)",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Gressling/S88-NG/tree/main/labforward-s88",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
