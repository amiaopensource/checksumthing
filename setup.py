from setuptools import setup
import sys

test_requirements = []
if sys.version_info[0] < 3:
    test_requirements.append('mock')

setup(
    name='Checksumthing',
    version='0.0.3',
    packages=['Checksumthing', 'Checksumthing.manifest_formats', 'scripts'],
    scripts=['scripts/checksumthing.py'],
    entry_points={
        'console_scripts': ['checksumthing=checksumthing:main']
    },
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://amiaopensource.github.io/checksumthing/',
    license='GPL3',
    author='Henry Borchers, Joshua Ng, Reto, Jonathan Farbowitz, Morgan Oscar Morel, Crystal Sanchez',
    author_email='',
    description='The ultimate checksum script! Checksumthing helps you create different kinds of checksum sidecar files'
)
