#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# quicksorts.py (C) myke, 2015
# 2015-11-08 1.1
# various versions  of quicksort alogo

import random

TIMES = 10
SIZE  = 10
RANGE = 10

# -----------------------------------------------
def qs1 (al):
    """ Algo quicksort for a list
    """
    if not al:
        return []

    return (qs1([x for x in al if x < al[0]])
        + [x for x in al if x == al[0]]
        + qs1([x for x in al if x > al[0]]))

# -----------------------------------------------
def qs2 (array):
    """ another longer version"""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return qs2(less)+equal+qs2(greater)
    else:
        return array


# -----------------------------------------------
qs = qs1

# -----------------------------------------------
def main ():
    """ dispatcher: tests make and sort """

    for i in range(TIMES):
        sa = [random.randint(1, RANGE) for e in range(SIZE)]
        print (sa, "-->", qs (sa))

main()

# -----------------------------------------------
# used: http://stackoverflow.com/questions/18262306/quick-sort-with-python
