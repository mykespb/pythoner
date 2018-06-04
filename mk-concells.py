#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-concells.py
#  find largest area of connected cells in rectangular matrix
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-04 0.1

# setting
NO_TESTS = 1
# size of  matrix
ROWS = 10
COLS = 10

# globals
mat = []


def generate():
    """fill the matrix"""
    global mat
    pass


def solve():
    """solve the problem"""
    global mat
    pass


def main(args):
    """runner"""
    for test in range(NO_TESTS):
        print("\n*** test", test, "***\n")
        generate()
        solve()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

