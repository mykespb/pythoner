#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-subsets1.py
#  print all subsets of a given ste
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-03 1.0

import random

# parameters
NO_TESTS = 3
MAX_ITEMS = 10
MAX_VALUE = 100


def prepare():
    """prepare a set"""

    src = set([random.randint(0, MAX_VALUE) for _ in range(random.randint(0, MAX_ITEMS))])
    print("source set =", src)
    return src


def multi(src):
    """make all subsets"""

    arr = sorted(list(src))
    larr = len(arr)
    print("sorted array =", arr)
    total = 2 ** larr
    print("array len =", larr, ", total variants =", total, "\n")

    for subn in range(total):
        sub = set()
        det = subn
        dig = 0
        while det:
            if det % 2 == 1:
                sub.add( arr[dig] )
            det //= 2
            dig += 1
        res = sorted(list(sub))
        print("sub#", subn+1, ", sub is", res)


def main(args):
    """main dispatcher"""

    for test in range(NO_TESTS):
        print()
        print(60*"=", "\n\ntest %d\n" % (test+1,))

        multi(prepare())

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

