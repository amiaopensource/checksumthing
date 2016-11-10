from setuptools import setup
import sys

test_requirements = []
if sys.version_info[0] < 3:
    test_requirements.append('mock')

setup(
    name='Checksumthing',
    version='0.0.1',
    packages=['Checksumthing', 'Checksumthing.manifest_formats'],
    scripts=['scripts/checksumthing.py'],
    entry_points={
        'console_scripts': ['checksumthing=checksumthing:main']
    },
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
