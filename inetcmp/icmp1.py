#!/usr/bin/env python
# -*- coding: utf-8 -*-

# icmp1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2021-12-31 2022-01-02 1.1

# берём страницу в инете, запоминаем фрагмент,
# а потом повторными запусками проверяем, изменилась ли страница в указанном месте

import os.path
import sys
import requests
from lxml import html as html
from collections import namedtuple

fstore = "icmp.tab"

Record = namedtuple("Record", "site pattern value last")

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

# ~ структура базы
# ~ site pattern value last


def getdata ():
    """
    считать данные в список
    """
    there = []
    
    with open(fstore) as store:
        for aline in store:
            line = line.strip()
            # ~ site, pattern, value, last = line.split()
            there.append(Record(line.split()))

    return there
    

if not os.path.isfile("./" + fstore):
    with open(fstore, 'w') as store:
        store.write("#site\tpattern\tvalue\tlast\n")

path = 'https://linuxmint.com'
patt = '//div/div/div/h2/text()'

given = path, patt

resp  = requests.get(path)
pbody = html.fromstring(resp.text)
elem  = pbody.xpath(patt)
print("Linux Mint version =", elem[0])
