from codecs import open as codecs_open
from setuptools import setup, find_packages
from md_autogen import __version__


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="md_autogen",
    version=__version__,
    description=u"API doc generator in markdown",
    long_description=long_description,
    author="raghakot",
    packages=find_packages(),
    test_suite="tests",
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov'
        ]
    },
)
