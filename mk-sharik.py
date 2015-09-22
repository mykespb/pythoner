#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# mk-sharik.py
# myke 2014-05-25 1.0
# поиск коробки (с 0) с макс числом цветов шариков

boxes = [ [1, 2, 2, 3, 1, 6, 6, 6, 7],
    [3, 3, 1, 8, 9, 3, 3, 1, 3, 8, 8, 8, 8, 8, 9, 9],
    [1, 1, 1, 1, 4, 4, 5, 2, 3, 6, 7, 8],
    [2, 2, 9, 8, 7, 2, 2, 2, 2] ]

def main():
    bosets = list(enumerate([len(set(x)) for x in boxes]))
    bosets.sort(key = lambda x: x[1])
    print "в коробке %d шарики %d цветов" % bosets[::-1][0]

main()
