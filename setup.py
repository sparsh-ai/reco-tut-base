from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'RecSys package'
LONG_DESCRIPTION = 'RecSys Python package for building and deploying recommender systems.'

setup(
    name="src", 
    version=VERSION,
    author="Sparsh Agarwal",
    author_email="recohut@gmail.com",
    url="https://github.com/sparsh-ai",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'recsys'],
    classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Topic :: Recommendation Systems :: Artificial Intelligence",
        ]
)