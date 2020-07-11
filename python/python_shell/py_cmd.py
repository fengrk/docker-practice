# coding:utf-8
__author__ = 'rk.feng'

import argparse


def echo_name(argv=None):
    parser = argparse.ArgumentParser(description='demo')

    # name
    parser.add_argument('--name', type=str, help='name')
    args = parser.parse_args(args=argv)
    print("name_{}".format(args.name))


if __name__ == '__main__':
    echo_name()
