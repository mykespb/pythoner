#!/usr/bin/env python
# -*- coding: utf-8 -*-

# icmp1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2021-12-31 2021-12-31 0.1

# берём страницу в инете, запоминаем фрагмент,
# а потом повторными запусками проверяем, изменилась ли страница в указанном месте

import os.path
import sys
import lxml

fstore = "icmp.tab"

help = """
This is icmp.py.
Usage:
    icmp
        show help
    icmp site pattern
        1st run:   read and store in icmp.tab
        next runs: compare and inform if there are diifs.
        note: only 1st pattern case is processed.
"""


def inbsase(psite, ppattern):
    """
    проверить, есть ли уже в базе такая строка.
    если да, то вернуть значение.
    если нет, то ''.
    """
    with open(fstore) as store:
        for aline in store:
            line = line.strip()
            site, pattern, value = line.split()
            if site == psite and pattern == pattern:
                return val
    return ""
    

def refind(psite, ppattern):
    """
    найти строку в инете и сравнить с сохранённой
    """
    ...

def store(psite, ppattern):
    """
    сохранить строку в базе
    """
    ...

if not os.path.isfile("./" + store):
    with open(fstore, 'w') as store:
        store.write("site\tpattern\tvalue\n")

if len(sys.argv) > 2:
    site, pattern = sys.argv[1:3]

        there = dofind(site, pattern)
        
        if inbase(cmd, s):
            refind(site, pattern)
        else:
            store(site, pattern)
else:
    print(help)
    exit(0)
