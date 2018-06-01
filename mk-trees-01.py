#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-trees-01.py 2018-04-27 0.2
#  Mikhail Kolodin, 2018-04
#  tests for trees etc

# Just adding old tests and problems for students of Python.

# ---------------------------

import random

# ---------------------------
# test 1
# ---------------------------

VALFROM = 0
VALTO   = 50
VALNUM  = 20

class Tree1:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        """add a unique value to tree"""
        if val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Tree1(val)
        elif val > self.val:
            if self.right:
                self.right.add(val)
            else:
                self.right = Tree1(val)

    def print(self):
        """ordered output"""
        if self.left:
            self.left.print()
        print(self.val, end=", ")
        if self.right:
            self.right.print()

    def exists(self, val):
        """test if value is in tree"""
        if val == self.val:
            return True
        if val < self.val and self.left:
            return self.left.exists(val)
        if val > self.val and self.right:
            return self.right.exists(val)
        return False

def test1():
    """create a tree and find a value"""
    tree = t1make(VALNUM)
    tree.print()
    t1find(tree)

def t1make(valnum):
    """make a tree"""
    r = random.randint(VALFROM, VALTO)
    print (f"adding {r}, ")
    t = Tree1(r)
    for i in range(1, valnum):
        r = random.randint(VALFROM, VALTO)
        print (f"adding {r}, ")
        t.add (r)
    return t

def t1find(tree):
    """find a value"""
    print()
    for i in range(VALNUM):
        r = random.randint(VALFROM, VALTO)
        print(f"Looking for {r}, result is {tree.exists(r)}")

# ---------------------------

def main(args):
    test1()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
