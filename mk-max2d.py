#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-max2d.py 2015-09-18 1.0
# (C) Mikhail Kolodin, 2015
# find max subarray in 2-dim array
# 1st version: w/o optimization!

from random import randint as ri

xsize = ysize = 3  # given parameters: matrix size
rmin, rmax = -10, 10 # min & max randoms

arr = [] # array to make & solve
vmax = 0 # max sum
xmax = ymax = 0 # submatrix ul corner
xlen = ylen = 0 # submatrix dimmensions

def makearr():
    """make sample array"""
    global arr
    arr = [[ri(rmin, rmax) for y in range(ysize)] for x in range(xsize)]
    print ("source matrix:")
    pp (arr)

def pp (mat):
    """print table"""
    for i in mat:
        for j in i:
            print("%5d " % j, end="")
        print()

def solvearr():
    """solve sample array"""
    global arr, xsize, ysize, vmax, xmax, ymax, xlen, ylen

    xmax = ymax = 0
    xlen = ylen = 1
    vmax = arr[0][0]

    for i in range(xsize):
        for j in range(ysize):
            #got upper left corner
            for xvar in range(xsize-i):
                for yvar in range(ysize-j):
                    #got dimensions
                    proc (i, j, xvar, yvar)

    print ("\nfound max sum: %d,\nupper left: %d:%d, dimensions: %d:%d" % (vmax, xmax, ymax, xlen+1, ylen+1))
    sub = [[i[j] for j in range (ymax, ymax+ylen+1)] for i in arr[xmax: xmax+xlen+1]]
    pp (sub)

def proc (up, left, xvar, yvar):
    """process subsum"""
    global arr, xsize, ysize, vmax, xmax, ymax, xlen, ylen
    vnew = subsum (up, left, xvar, yvar)
    if vnew > vmax:
        vmax = vnew
        xmax = up
        ymax = left
        xlen = xvar
        ylen = yvar

def subsum (up, left, xvar, yvar):
    """calc submatrix sum"""
    s = 0
    for i in range (up, up+xvar+1):
        for j in range (left, left+yvar+1):
            s += arr[i][j]

    return s

def main():
    """mian fun"""
    makearr()
    solvearr()

main()


#~ source matrix:
   #~ -6   -10    -6
   #~ -7     3     9
    #~ 5     2    -9

#~ found max sum: 12,
#~ upper left: 1:1, dimensions: 1:2
    #~ 3     9


#~ source matrix:
    #~ 1     4    -8     6     7     7    -2    -7    -9     1
   #~ -5    -1     2     2    -5    -7     7    -9     0    -6
    #~ 2    -1    -1     1    -6    -9    -5    -1    -3     1
   #~ -4   -10     8    -5     3    -8    -8     5    -8     9
   #~ 10     1     8     9    -1     5    -2    -5    -6     6
    #~ 2     0   -10     9     1    10    -2    10     3    -1
    #~ 8     9    -6     0     3     1    -2   -10     1     7
   #~ -8     3    -7     9   -10    -3    -6     6    -7     0
    #~ 4     1     0     4     2     9     6    10    -1   -10
   #~ -8     2   -10    -3     3     1     2    -3     0     7

#~ found max sum: 68,
#~ upper left: 4:0, dimensions: 5:8
   #~ 10     1     8     9    -1     5    -2    -5
    #~ 2     0   -10     9     1    10    -2    10
    #~ 8     9    -6     0     3     1    -2   -10
   #~ -8     3    -7     9   -10    -3    -6     6
    #~ 4     1     0     4     2     9     6    10


#~ source matrix:
   #~ 96    35   -76    52   -91    96    96   -37    72   -97
  #~ -55    -8    25    83   -60    25     3   -15   -36   -23
   #~ 47    37   -70    70    86   -65   -96    16    35    71
   #~ -1   -86    91   -60    77    59     7    -7    51   -91
  #~ -83    52   -43   -15    77   -91   -41    15   -88   -16
  #~ -80   -96    41    99    78    15   -93    63    78   -62
   #~ 28    65   -12   -83   -66    52   -63   -63     4    21
   #~ 39    32    -4    76   -81   -40    75    50    31   -93
    #~ 8    54   -18   -96   -57   -67   -58   -14   -96   -52
   #~ 18   -29   -21   -18    92    43   -37    90    -4    60

#~ found max sum: 479,
#~ upper left: 1:2, dimensions: 5:3
   #~ 25    83   -60
  #~ -70    70    86
   #~ 91   -60    77
  #~ -43   -15    77
   #~ 41    99    78
