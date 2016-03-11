#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mk-rot.py 2016-03-11 2016-03-11 1ю0
# rot cypher, for English & Russian, auto

latbig   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
latsmall = "abcdefghijklmnopqrstuvwxyz"
rusbig   = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
russmall = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = "hello to all всем привет И ТАК ПОБЕДИМ AND THIS WAY"

def alf (c, s):
    """ change for 1 alfabet """
    if c in s:
        return s[ (s.index(c) + len(s)//2 ) % len(s) ]
    return False

def rot (t):
    """ rotate text """
    r = ""
    for c in t:
        r += (alf (c, latbig) or
              alf (c, latsmall) or
              alf (c, rusbig) or
              alf (c, russmall) or
             c)
    return r

def main(args):
    """ do all """
    print ("source test = %s\ncoded text  = %s\nback text   = %s\n" %
        (text, rot(text), rot(rot(text))))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
