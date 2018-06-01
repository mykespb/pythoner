#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-graphs1.py
#  tests with graphs: create a sample graph and parse it in different ways
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-05-31 1.1

# graph representations:
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

import string
import random

# data = string for experiments
alf = string.ascii_uppercase

# main parameteres of experiments

NO_TESTS = 10    # used in main function
NO_LINKS = 10    # recalc in run function
NO_NODES = 10    # recalc in run function
MULT_LINKS = 3   # multiplier for #links from #nodes

# ---------------------------------------
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

def run1():
    """make group of tests with repr 1"""

    global NO_NODES, NO_LINKS
#    NO_NODES = 6
#    NO_LINKS = 5
    NO_NODES = random.randint(5, len(alf))
    NO_LINKS = random.randint(0, NO_NODES*3)
    walf = alf[:NO_NODES]
    print ("nodes =", NO_NODES, ", links =", NO_LINKS, ", alf =", walf)

    g = g1fill(walf)
    res = g1test(g, walf)
    print ("congratulations" if res else "condolences")


def g1fill(walf):
    """fill sample graph from alphabet walf,
    return graph
    """

    links = set()
    for n in range(NO_LINKS):
        node1 = random.choice(walf)
        node2 = random.choice(walf)
        if node1 == node2: continue
        links.add((node1, node2))
    print ("links =", links)

    return links


def g1test(links, walf):
    """test sample graph,
    take graph,
    return true/false
    """

    node1 = random.choice(walf)
    node2 = random.choice(walf)
    print ("looking for path from", node1, "to node", node2)

    res, way = g1dfs(links, walf, node1, node2)
#    res, lth, way = g1bfs(g, walf)
    if res:
        print ("way found: length =", len(way)-1, ", nodes are", way)
    else:
        print ("no way found, alas")

    return res


def g1dfs(links, walf, node1, node2):
    """find any way between 2 nodes, by depth first search,
    and return result, length of way, way itself
    """

    # make symmetrtic links set, because we have non-directional (non-oriented) graph
    links1 = set()
#    links0 = links
    for el in links:
        links1.add((el[1], el[0]))
    links |= links1
 #   print ("debug:\n", links, "\n", links0, "\n", links1)

    # print matrix
    print ("\n ", walf)
    for c1 in walf:
        print (c1, end=" ")
        for c2 in walf:
            print ("+" if (c1, c2) in links else "\\" if c1 == c2 else ".", end="")
        print("", c1)
    print(" ", walf, "\n")

    # do find a way
    way = [node1]
    return g1dfsWay(links, way, node1, node2)


def g1dfsWay(links, way, node1, node2):
    """find a way and return it with True,
    or say False
    """
    print ("debug:", way, node1, node2)

    # trivial task
    if node1 == node2:
        return True, way

    # check if we found a way
    if (node1, node2) in links:
        way.append(node2)
        return True, way

    # we try to continue our way
    for nextnode in links:
        if nextnode[0] == node1 and nextnode[1] not in way:
            way.append(nextnode[1])
            ares, away = g1dfsWay(links, way, nextnode[1], node2)
            if ares:
                return True, away
            way = way[:-1]

    return False, way


# ---------------------------------------

def main(args):
    for test in range(NO_TESTS):
        print ("\ntest %d" % (test+1,))
        run1()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
