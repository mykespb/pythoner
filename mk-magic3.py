#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# mk-magic3.py
# myke 2014-05-25 1.1
# построение всех магических квадратов 3 порядка, 2 способами

import itertools

def ismagic (l):
    """ test if combination is magic """
    return (
        l[0]+l[1]+l[2] ==
        l[3]+l[4]+l[5] ==
        l[6]+l[7]+l[8] ==
        l[0]+l[3]+l[6] ==
        l[1]+l[4]+l[7] ==
        l[2]+l[5]+l[8] ==
        l[0]+l[4]+l[8] ==
        l[2]+l[4]+l[6] )

def show(l):
    """ show magic square """
    print (u"магический квадрат:\n")
    print ("%3d %3d %3d \n%3d %3d %3d \n%3d %3d %3d\n" %
        (l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))

def main1():
    print "magic3.1\n"
    lst = list(itertools.permutations(range(1, 10), 9))
    for comb in lst:
        if ismagic(comb):
            show(comb)
            #~ i=raw_input()

def main2():
    print "magic3.2\n"
    lst = [l for l in list(itertools.permutations(range(1, 10), 9)) if ismagic(l)]
    for i, l in list(enumerate(lst)):
        print (u"--- решение %d ---\n%3d %3d %3d \n%3d %3d %3d \n%3d %3d %3d\n" %
            (i+1, l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))

main2()

#~ magic3.2
#~
#~ --- решение 1 ---
  #~ 2   7   6
  #~ 9   5   1
  #~ 4   3   8
#~
#~ --- решение 2 ---
  #~ 2   9   4
  #~ 7   5   3
  #~ 6   1   8
#~
#~ --- решение 3 ---
  #~ 4   3   8
  #~ 9   5   1
  #~ 2   7   6
#~
#~ --- решение 4 ---
  #~ 4   9   2
  #~ 3   5   7
  #~ 8   1   6
#~
#~ --- решение 5 ---
  #~ 6   1   8
  #~ 7   5   3
  #~ 2   9   4
#~
#~ --- решение 6 ---
  #~ 6   7   2
  #~ 1   5   9
  #~ 8   3   4
#~
#~ --- решение 7 ---
  #~ 8   1   6
  #~ 3   5   7
  #~ 4   9   2
#~
#~ --- решение 8 ---
  #~ 8   3   4
  #~ 1   5   9
  #~ 6   7   2
