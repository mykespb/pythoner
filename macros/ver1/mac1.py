#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mac1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-04 2022-01-04 1.0
# see description below.

import fileinput

macs = {}

files = 'in1.txt',

for aline in fileinput.input(files=files, encoding = "utf-8"):
    line = aline.strip()

    if line.startswith('$'):
        key, val = line[1:].split('=', 2)
        macs[key] = val

    else:
        for key, val in macs.items():
            line = line.replace('${'+key+'}', val)
        print (line)


# ~ Description
# ~ --------------------------------------

# ~ Text file contains text that is probably a program.

# ~ It also has lines like
# ~ $name=text

# ~ and every time construction ${name} occurs in the text
# ~ it is substituted my corresponding text.

# ~ It reads from stdin, or given files,
# ~ writes to stdout.

# ~ Restrictions
# ~ --------------------------------------

# ~ No recursion (so far).
# ~ No parameteres (so far).
# ~ To be done in following versions.
