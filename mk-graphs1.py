#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mk-graphs1.py
#  tests with graphs: create a sample graph and parse it in different ways

# graph representations:
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

import string
import random

alf = string.ascii_uppercase

NO_TESTS = 10
NO_LINKS = 10

# ---------------------------------------
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

g1 = set()


def run1():
    """make group of tests with repr 1"""
    global NO_LINKS
    NO_LINKS = random.randint(5, len(alf)- 5)
    g1fill()
    g1test()

def g1fill():
    """fill sample graph"""
    pass

def g1test():
    """test sample graph"""
    print (NO_LINKS, alf[:NO_LINKS])

# ---------------------------------------

def main(args):
    for test in range(NO_TESTS):
        run1()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
