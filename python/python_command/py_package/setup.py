# -*- coding: utf-8 -*-
from setuptools import setup

# version info
NAME = "py_package"
VERSION = "0.4.0"
DESC = "py_package"

# setup config
setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=DESC,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    install_requires=[],
    author="frkhit",
    url="",
    author_email="",
    license="",
    packages=["py_package", "py_package.a", "py_package.cmd"],
    package_data={
        "": ["README.md", "MANIFEST.in"],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'py_package_print = py_package.info:print_package',
            'py_package_print_a = py_package:print_a'
        ]
    },
)
