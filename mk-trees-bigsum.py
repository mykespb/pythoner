#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-trees-bigsum.py 2023-07-23 2023-07-23 1.0
# 1. make trees
# 2. input data
# 3. find deep biggest sum

class Node:

    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """print it"""

        sout = "( "
        sout += str(self.value) + ", "
        if self.left:
            sout += self.left.__str__()
        if self.right:
            sout += self.right.__str__()
        sout += " ), "
        return sout
    
    def make(self, loi) -> None:
        """fill from given data"""

        self.value = loi[0]
        if len(loi) > 1:
            noda = Node()
            noda.make(loi[1])
            self.left = noda
        if len(loi) > 2:
            noda = Node()
            noda.make(loi[2])
            self.right = noda


def solve(loi) -> int:
    """find biggest sum"""

    tree = Node()
    tree.make(loi)
    # print(tree)

    return go(tree)


def go(tree):
    """run deep"""

    if tree is None: return 0

    return tree.value + max(go(tree.left), go(tree.right))


def test(loi):
    """print it and run test"""

    print(f"{loi=} => {solve(loi)}")


test([1, 
        [4, 
            [2, 
                [3, 
                    [2]] ]],
        [7, 
            [5], 
            [4]]
    ])        

test([1])

test([1, [2], [3]])

test([1, [2, [5]], [3]])

# loi=[1, [4, [2, [3, [2]]]], [7, [5], [4]]] => 13
# loi=[1] => 1
# loi=[1, [2], [3]] => 4
# loi=[1, [2, [5]], [3]] => 8

# ( 1, ( 4, ( 2, ( 3, ( 2,  ),  ),  ),  ), ( 7, ( 5,  ), ( 4,  ),  ),  ), 
# loi=[1, [4, [2, [3, [2]]]], [7, [5], [4]]] => 13
# ( 1,  ), 
# loi=[1] => 1
# ( 1, ( 2,  ), ( 3,  ),  ), 
# loi=[1, [2], [3]] => 4
# ( 1, ( 2, ( 5,  ),  ), ( 3,  ),  ), 
# loi=[1, [2, [5]], [3]] => 8
