#!/bin/sh

# install package
cd /app/py_package && pip install .

# python -m
cd /app
echo -e "\n\nexec:\tpython -m py_package xxxx"
python -m py_package xxxx

echo -e "\n\nexec:\tpython -m py_package.a yyyy"
python -m py_package.a  yyyy

# script
echo -e "\n\nexec:\tpy_package_print"
py_package_print

echo -e "\n\nexec:\tpy_package_print_a"
py_package_print_a





