#!/bin/sh


name="M 1 M"


c1=$(python py_cmd.py --name='${name}' )
echo "case1 ${c1}"

c2=$(python py_cmd.py --name="${name}" )
echo "case2 ${c2}"

c3=$(python py_cmd.py --name="$name" )
echo "case3 ${c3}"


