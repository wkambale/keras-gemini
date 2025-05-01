from setuptools import setup, find_packages

setup(
    name="keras-gemini",
    version="0.1.2",
    description="A Python package that combines the power of Keras with Gemini for natural language-driven neural network building.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wkambale/keras_gemini",
    author="Wesley Kambale",
    author_email="spartanwk@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "keras",
        "gemini-python",
        "nltk"
    ],
    tests_require=[
        'pytests>=6.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
