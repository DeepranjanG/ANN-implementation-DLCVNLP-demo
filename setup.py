from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="DeepranjanG",
    description="A small package for ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepranjanG/ANN-implementation-DLCVNLP-demo",
    author_email="kd082442@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow-cpu==2.2.0",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)