#! /usr/bin/env python3

# print JSON file indented
# Mikhail (myke) Kolodin, 2020
# 2020-12-21 1.0

import json
import sys

indent = 4

if (len(sys.argv) == 2 and 
    (sys.argv[1] == "-h" or
    sys.argv[1] == "--help")):
    print("""
This is mkJSONer.
Use:
mkjsoner -h   or --help
    show this message;
mkjsoner from_file to_file
    take json object from from_file and print it to to-file;
You may specify '-' as from_file or to_file for console IO.
    """)
    exit(0)

if len(sys.argv) < 2:
    fin = '-'
    fout = '-'
elif len(sys.argv) < 3:
    fin = sys.argv[1]
    fout = '-'
else:
    fin, fout = sys.argv[1], sys.argv[2]

if fin == '-':
    si = ""
    sii = input()
    try:
        while sii:
            si += sii
            sii = input()
    except:
        pass
else:
    with open(fin) as fi:
        si = json.load(fi)

if fout == '-':
    json.dump(si, sys.stdout, indent=indent)
else:
    with open(fout, 'w') as fo:
        json.dump(si, fo, indent=indent)
