from setuptools import setup

setup(
    name='Checksumthing',
    version='0.0.1',
    packages=['Checksumthing'],
    scripts=['scripts/checksumthing.py'],
    entry_points={
        'console_scripts': ['checksumthing=checksumthing:main']
    },
    zip_safe=False,
    test_suite='tests',
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
