from setuptools import setup


setup(
    name='myvariant-api',
    version='1.0',
    author='Brian Schrader',
    author_email='brian@biteofanapple.com',
    packages=['myvariant', 'tests'],
    scripts=[], # TODO: Add bin/ scripts here.
    license='LICENSE.txt',
    description='A simple API wrapper for the MyVariant.info API.',
    keywords=['variant', 'genomics'],
    install_requires=[
        'requests'
        ]
    )
