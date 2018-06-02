#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-subsets1.py
#  print all subsets of a given ste
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-02 0.1

NO_TESTS = 3
MAX_ITEMS = 10

src = set()

def prepare():
    """prepare a set"""
    pass


def multi():
    """make all subsets"""
    pass


def show():
    """print all subsets"""
    pass


def main(args):
    """main dispatcher"""

    for test in range(NO_TESTS):
        print()
        print(60*"=", "\n\ntest %d" % (test+1,))
        prepare()
        multi()
        show()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
