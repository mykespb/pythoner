#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mk-tries1.py
#  data structure for storing words as chains.
#  here we create a class, add words, output them, and search for them
#
#  See also: https://www.youtube.com/watch?v=zIjfhVPRZCg
#  "Data Structures: Tries"
#
#  (C) Mikhail Kolodin, 2018
#  ver. 2018-06-02 0.1

class Trie:
    """class for Trie"""

    def __init__(self, data=None):
        self.data =''
        self.links = {}
        self.stop = True
        if data:
            self.add(data)

    def add(self, data):
        """add word to trie"""
        #TODO
        pass

    def __repr__(self):
        """show me"""
        #TODO
        pass

    def has(self, data):
        """say if data is in trie"""
        #TODO
        pass

def main(args):

    t = Trie()
    print(t)

    t.add("CALL")
    t.add("CITY")
    t.add("CAT")
    print(t)

    test_set = "CASE", "CITY", "FINAL", "CAT"

    for test in test_set:
        print("test if", test, "is in trie gives", t.has(test))

    t = Trie("CUTTY")
    print(t)

    t.add("FINITA")
    print(t)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
