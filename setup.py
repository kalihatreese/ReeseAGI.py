from setuptools import setup, find_packages

setup(
    name='ReeseAGI',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'reeseagi=ReeseAGI.main:main',
        ],
    },
)