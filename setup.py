from setuptools import setup, find_packages


setup(
    name='util_funcs',
    version='0.1',
    description='Some useful python utility functions',
    
    # Main homepage
    url='https://github.com/secnot/python-util-funcs/',
    
    # Extra info and author details
    author='SecNot',

    keywords=['utils',],

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Natural Language :: English',
        ],

    # package
    packages = ['util_funcs'],
    install_requires = [],
    zip_safe = False,

    # Tests
    test_suite='nose.collector',
    tests_require=['nose'],
)
