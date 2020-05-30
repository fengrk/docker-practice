# coding:utf-8
__author__ = 'rk.feng'

import os

_cur_dir = os.path.dirname(__file__)


def print_package():
    _file_list = ["\t{}".format(_file) for _file in os.listdir(_cur_dir)]
    print("file in py_package/:\n{}\n".format("\n".join(_file_list)))
