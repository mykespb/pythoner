#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# mk-pi-estim.py

from __future__ import division
import random, math

func = lambda x, y: math.sqrt(x*x + y*y) <= 1.0

#~ calc = 0

def deep (n, x0, y0, x1, y1):
    """ calc for sqaure x0, y0 - x1, y1 """
    global calc
    xp = x0 + (x1-x0)/2
    yp = y0 + (y1-y0)/2
    res = func (xp, yp)
    calc += 1
    if n:
        res += (deep (n-1, x0, y0, xp, yp) +
            deep (n-1, xp, y0, x1, yp) +
            deep (n-1, x0, yp, xp, y1) +
            deep (n-1, xp, yp, x1, y1))
    return res

def sqatest():
    """ organize square test """
    global calc
    for n in xrange(1, 12):  # 13=max! :)
        calc = 0
        val = deep (n, 0, 0, 1, 1) * 4.0 / calc
        print ("deep = %d => pi = %20.15f" % (n, val))

def estim (rept=1):
    """ calc random estimation for pi """
    c = 0
    for i in xrange(rept):
        x, y = random.random(), random.random()
        c += func (x, y)
    c *= 4
    print ("rept: %10d => pi=%20.15f" % (rept, c/rept))

def randtest():
    """ organize random test """
    for rept in 100, 1000, 10000, 100000, 1000000, 10000000:
    #~ for rept in 100, 1000, 10000, 100000, 1000000:
        estim(rept)

def main():
    """ general switcher """
    randtest()
    sqatest()
    return 0

if __name__ == '__main__':
    main()

#~ rept:        100 => pi=   3.000000000000000
#~ rept:       1000 => pi=   3.096000000000000
#~ rept:      10000 => pi=   3.110800000000000
#~ rept:     100000 => pi=   3.149080000000000
#~ rept:    1000000 => pi=   3.141416000000000
#~ rept:   10000000 => pi=   3.141264800000000
#~ deep = 1 => pi =    3.200000000000000
#~ deep = 2 => pi =    3.238095238095238
#~ deep = 3 => pi =    3.247058823529412
#~ deep = 4 => pi =    3.190615835777126
#~ deep = 5 => pi =    3.161904761904762
#~ deep = 6 => pi =    3.151071232375023
#~ deep = 7 => pi =    3.143785763332570
#~ deep = 8 => pi =    3.142193383000881
#~ deep = 9 => pi =    3.141863958229025
#~ deep = 10 => pi =    3.141724381857963
#~ deep = 11 => pi =    3.141625114776201

