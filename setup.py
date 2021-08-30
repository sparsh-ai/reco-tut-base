from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'RecSys package'
LONG_DESCRIPTION = 'RecSys Python package for building and deploying recommender systems.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="src", 
        version=VERSION,
        author="Sparsh Agarwal",
        author_email="recohut@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'recsys'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)