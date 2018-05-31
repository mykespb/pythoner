#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-graphs1.py
#  tests with graphs: create a sample graph and parse it in different ways
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-05-31 0.1

# graph representations:
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

import string
import random

# data = string for experiments
alf = string.ascii_uppercase

# main parameteres of experiments

NO_TESTS = 1     # used in main function
NO_LINKS = 10    # recalc in run function
NO_NODES = 10    # recalc in run function

# ---------------------------------------
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

def run1():
    """make group of tests with repr 1"""

    global NO_NODES, NO_LINKS
    NO_NODES = random.randint(5, len(alf))
    NO_LINKS = random.randint(0, NO_NODES*2)
    walf = alf[:NO_NODES]
    print ("nodes=", NO_NODES, ", links=", NO_LINKS, ", alf=", walf)

    g = g1fill(walf)
    res = g1test(g, walf)
    print ("congratulations" if res else "condolences")


def g1fill(walf):
    """fill sample graph from alphabet walf,
    return graph
    """

    g = set()
    for n in range(NO_LINKS):
        g.add((random.choice(alf), random.choice(alf)))
    print ("task=", g)

    return g


def g1test(g, walf):
    """test sample graph,
    take graph,
    return true/false
    """

    node1 = random.choice(walf)
    node2 = random.choice(walf)
    print ("looking for path from", node1, "to node", node2)

    res, lth, way = g1dfs(g, walf, node1, node2)
#    res, lth, way = g1bfs(g, walf)
    if res:
        print ("way found: length =", lth, ", nodes are", way)
    else:
        print ("no way found, alas")

    return res


def g1dfs(g, walf, node1, node2):
    """find any way between 2 nodes, by depth first search,
    and return result, length of way, way itself
    """


    return False, 0, []


# ---------------------------------------

def main(args):
    for test in range(NO_TESTS):
        print ("\ntest %d" % (test+1,))
        run1()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
