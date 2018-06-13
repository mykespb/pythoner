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
#  ver. 2018-06-13 0.4

class Trie:
    """class for Trie"""

    def __init__(self, data=None):
        """create new node"""
        self.links = {}
        if data:
            self.add(data)


    def add(self, data):
        """add word to trie"""

        if not data: return

        cch = data[0]
        cdata = data[1:]
        cnode = self

        if len(cdata) == 0:

            if cch in cnode.links:
                if '' not in cnode.links[cch].links:
                    cnode.links[cch].links[''] = None
                return
            else:
                cnode.links[cch] = Trie()
                return

        else:

            while cch in self.links:
                cnode = cnode.links[cch]
                cch = cdata[0]
                cdata = cdata[1:]

            nnode = Trie(cdata)
            cnode.links[cch] = nnode
            # ~ return


    def has(self, data):
        """say if data is in trie"""
        #TODO
        pass


    def delete(self, value):
        """delete word"""
        pass


    def __repr__(self):
        """internal repr"""
        return self.links


    def __str__(self):
        """printable show"""
        if not self.links:
            return '()'
        out = '(' + self.allstrings() + ')'
        return out


    def allstrings(self):
        """give all strings, separated by commas"""
        if not self.links:
            return ""
        out = ''
        for c, link in self.links.items():
            if c:
                out += c
                if link:
                    out += link.allstrings()
                else:
                    out += ', '
            else:
                out += ', '
        return out


def main(args):

    t = Trie()

    t.add("A")
    print(t)
    t.add("TO")
    print(t)
    t.add("TAR")
    print(t)
    t.add("TARAN")
    print(t)
    t.add("TOOLS")
    print(t)
    t.add("TOOL")
    print(t)
    t.add("CAT")
    print(t)
    t.add("AN")
    print(t)
    t.add("ANNA")
    print(t)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
