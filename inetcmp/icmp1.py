#!/usr/bin/env python
# -*- coding: utf-8 -*-

# icmp1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2021-12-31 2021-12-31 0.1

# берём страницу в инете, запоминаем фрагмент,
# а потом повторными запусками проверяем, изменилася ли страница в указанном месте

import sys
import lxml

store = "icmp.txt"

help = """
This is icmp.py.
Usage:
    icmp
        show help
    icmp page
        1st run:   read and store in icmp.txt
        next runs: compare and inform if there are diifs
"""


def inbsase(cmd):
    """
    проверить, есть ли уже в базе такая строка
    """
    ...

def refind(cmd):
    """
    найти строку в инете и сравнить с сохранённой
    """
    ...

def store(cmd):
    """
    сохранить строку в базе
    """
    ...

if len(sys.argv) >1:
    cmd = sys.argv[1]
    if cmd.startswith(('-h', 'help')):
        print(help)
        exit(0)
    else:
        if inbase(cmd):
            refind(cmd)
        else:
            store(cmd)
else:
    print(help)
    exit(0)

