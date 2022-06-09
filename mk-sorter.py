#!/usr/bin/env python3
# myke mk-sorter.py 2015-11-19 1.5
# 2018-04-13 added quick sort, slow version
# 2018-04-24 added timings
# 2019-04-04 funny sort newmin
# classic selection, bubble, quick sorts

import random
from datetime import datetime

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

def quicksort (a):
    """quick sorter"""

    if len(a) <= 1:
        return a
    else:
        return quicksort ([e for e in a[1:] if  e < a[0]]) + [a[0]] + quicksort([e for e in a[1:] if e >= a[0]])

# 1. a[0] as pivot value
# 2. not too fast :) due to making additional lists recursively

# -----------------------------------------------

def bubblesort (a):
    """ another bubbler"""

    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]>a[j]:
                s = a[j]
                a[i+1:j+1] = a[i:j]
                a[i] = s
    return a

# -----------------------------------------------

def newmin (a):
    """ new list and min function"""

    b = []
    c = a[:]
    while c:
        e = min(c)
        c.remove(e)
        b += [e]
    return b

# -----------------------------------------------
# ~ qs = bubsort
# ~ qs = selsort
# ~ qs =  quicksort
# ~ qs =  bubblesort
qs = newmin

# -----------------------------------------------
def main ():
    """ dispatcher: tests make and sort """

    total_before = datetime.now()

    for i in range(TIMES):
        sa = [random.randint(-RANGE, RANGE) for e in range(SIZE)]
        print (sa, end=" -> ")
        print (qs (sa))

    total_after = datetime.now()
    total_elapsed = total_after - total_before
    print ("Total time elapsed: {}" .format (total_elapsed))

main()

# ===============================================
