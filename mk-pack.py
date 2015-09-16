#!/usr/bin/env python
# -*- coding: utf-8 -*-
# задача о рюкзаке
# набрать вес ровно fit предметами из списка mass
# (любым способом, или  сказать, что нельзя)
# (C) myke 2015-03-04

def packit (fit, mass):
    print "\nPacking", fit, "from", mass
    sols = 0

    for v in xrange(2**len(mass)):
        if good (v, mass, fit):
            sols += 1
#            break
    print "Found", sols, "solutions"

def good (v, mass, fit):
    s = 0
    for i in xrange(len(mass)):
        if v & (2**i):
            s += mass[i]
            if s > fit:
                return False
    if s == fit:
        print "ok:", fit, "=",
        for i in xrange(len(mass)):
            if v & (2**i):
                print mass[i], ",",
        print
        return True
    else:
        return False

def main():
    packit (20, (10, 5, 15, 11, 9, 34))
    packit (20, (1, 2, 34, 5, 11, 8, 4))
    packit (10, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#    packit (10, (1, 1, 5, 5, 5, 9, 1, 1, 1))
#    packit (10, (5, 6, -1, 2))
    packit (8, (1, 1, 11, 22))
    return 0

main()

# --------------------------------------------------------
#Packing 20 from (10, 5, 15, 11, 9, 34)
#ok: 20 = 5 15
#ok: 20 = 11 9
#Found 2 solutions

#Packing 20 from (1, 2, 34, 5, 11, 8, 4)
#ok: 20 = 1 11 8
#ok: 20 = 5 11 4
#ok: 20 = 1 2 5 8 4
#Found 3 solutions

#Packing 10 from (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#ok: 10 = 1 2 3 4
#ok: 10 = 2 3 5
#ok: 10 = 1 4 5
#ok: 10 = 1 3 6
#ok: 10 = 4 6
#ok: 10 = 1 2 7
#ok: 10 = 3 7
#ok: 10 = 2 8
#ok: 10 = 1 9
#ok: 10 = 10
#Found 10 solutions

#Packing 8 from (1, 1, 11, 22)
#Found 0 solutions
