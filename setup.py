from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='WATER_SORT_PUZZLE',
    version='1',
    packages=['WATER_SORT_PUZZLE'],
    url='https://github.com/GlobalCreativeCommunityFounder/WATER_SORT_PUZZLE',
    license='MIT',
    author='GlobalCreativeCommunityFounder',
    author_email='globalcreativecommunityfounder@gmail.com',
    description='This package contains implementation of the game "WATER_SORT_PUZZLE" on command line interface.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "WATER_SORT_PUZZLE=WATER_SORT_PUZZLE.water_sort_puzzle:main",
        ]
    }
)