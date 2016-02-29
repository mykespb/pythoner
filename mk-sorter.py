#!/usr/bin/env python3
# myke mk-sorter.py 2015-11-13 1.3
# classic selection and bubble sortings

import random

TIMES = 10
SIZE  = 10
RANGE = 10

print ("hello sorter")

# -----------------------------------------------

def selsort (a):
    """selection sorter"""

    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

# -----------------------------------------------

def bubsort (a):
    """bubble sorter"""

    need = True
    while need:
        need = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                need = True
    return a

# -----------------------------------------------
#qs = bubsort
qs = selsort

# -----------------------------------------------
def main ():
    """ dispatcher: tests make and sort """

    for i in range(TIMES):
        sa = [random.randint(-RANGE, RANGE) for e in range(SIZE)]
        print (sa, end=" -> ")
        print (qs (sa))

main()

# ===============================================

