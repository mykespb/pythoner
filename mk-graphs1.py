#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-graphs1.py
#  tests with graphs: create a sample graph and parse it in different ways
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-01 1.5

# graph representation:
# set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

import string
import random

# data = string for experiments
alf = string.ascii_uppercase

# main parameteres of experiments

DEBUG = True     # print internal info
NO_TESTS = 9     # used in main function
NO_LINKS = 10    # recalc in run function
NO_NODES = 10    # recalc in run function
MULT_LINKS = 4   # multiplier for #links from #nodes

# ---------------------------------------
# 1. set of tuple-pairs, { (from, to), ...} -- not directed, not weighted

def run():
    """make group of tests with repr 1"""

    global NO_NODES, NO_LINKS

# test values
#    NO_NODES = 4
#    NO_LINKS = 4

# real life values
    NO_NODES = random.randint(5, len(alf))
    NO_LINKS = random.randint(0, NO_NODES*MULT_LINKS)

    walf = alf[:NO_NODES]
    print ("nodes =", NO_NODES, ", links =", NO_LINKS, ", alf =", walf)

    g = fill(walf)
    res = test(g, walf)
    print ("\n*** congratulations ***" if res else "\n*** condolences ***")


def fill(walf):
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


def test(links, walf):
    """test sample graph,
    take graph,
    return true/false
    """

    node1 = random.choice(walf)
    node2 = random.choice(walf)
    print ("looking for path from", node1, "to node", node2)

    links = relink(links, walf)

    # find way using depth first search
    res, way = dfs(links, walf, node1, node2)
    if res:
        print ("way found: length =", len(way)-1, ", nodes are", way)
    else:
        print ("no way found, alas")

    # find way using broadth (width) first search
    res = bfs(links, walf, node1, node2)
    if res:
        print ("way found, hurra :)")
    else:
        print ("no way found, alas :(")

    return res


def relink(links, walf):
    """complete pairs and print matrix"""

    # make symmetrtic links set, because we have non-directional (non-oriented) graph
    links1 = set()
    for el in links:
        links1.add((el[1], el[0]))
    links |= links1
    del links1

    # print matrix
    print ("\n ", walf)
    for c1 in walf:
        print (c1, end=" ")
        for c2 in walf:
            print ("+" if (c1, c2) in links else "\\" if c1 == c2 else ".", end="")
        print("", c1)
    print(" ", walf)

    return links


def dfs(links, walf, node1, node2):
    """find any way between 2 nodes, by depth first search,
    and return bool result, way itself
    """
    print ("\n*** solve the task by DFS ***")

    # do find a way
    way = [node1]
    return dfsWay(links, way, node1, node2)


def dfsWay(links, way, node1, node2):
    """find a way and return it with True,
    or say False
    """
    if DEBUG:
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
            ares, away = dfsWay(links, way, nextnode[1], node2)
            if ares:
                return True, away
            way = way[:-1]

    return False, way


def bfs(links, walf, node1, node2):
    """find any way between 2 nodes, by broadth (width) first search,
    and return bool result, without way itself
    """
    print ("\n*** solve the task by BFS ***")

    # do find a way
    nexts = [node1]
    curnode = node1
    way = []

    while nexts:
        curnode = nexts.pop(0)
        if DEBUG:
            print("debug current:", curnode)

        if curnode == node2:
            return True

        for n in links:
            if n[0] == curnode and n[1] not in way and n[1] != curnode and n[1] not in nexts:
                way.append(curnode)
                nexts.append(n[1])
                if DEBUG:
                    print("debug added:", n[1])

    return False


# ---------------------------------------

def main(args):
    """main dispatcher"""

    for test in range(NO_TESTS):
        print()
        print(60*"=", "\n\ntest %d" % (test+1,))
        run()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
