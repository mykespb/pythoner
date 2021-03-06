#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hily 2018-05-06 M.Kolodin 2018-05-13 1.0
# Highly Likely Project

# ver. 1. it must scan folders in hily.ini and print result (same files) into file hily.out.

# 1st ver. will work with sorted list of tiples
# 2nd ver. will use databases
#import sqlite3

# make pretty result
from pprint import pprint

# classic files access library
import os.path

# aux aim is to study modern library
from pathlib import Path

# ------------------------------------ config
# file with config
CONFIG = "hily.ini"

# folders list
flist = []

# outfile with pretty printed result, with default value
outfile = "./outfile.txt"

# result list with all info about files and foders
res = []

# ------------------------------------ start

def good_config ():
    """read configuration and cry if none or wrong."""

    global flist, outfile

    print ("Looking for configuration file.")

    if os.path.isfile (CONFIG):
        with open (CONFIG) as config:
            for line in config:
                line = line.strip ()
                if len (line):
                    print (line)
                    cmd, data = line.split (maxsplit=1)
                    if cmd == "in":
                        extdata = os.path.abspath (data)
                        flist += [extdata]
                    elif cmd == "out":
                        outfile = os.path.abspath (data)
        print (f"\nFolders list is {flist},\nresult will be written to {outfile}.")

        if not flist:
            print ("Folders list is empty. No work is possible. Quitting.")
            return False

    else:
        print (f"Config file {CONFIG} does not exist. Quitting.")
        return False

    return True

# ------------------------------------ init_db

# ~ def init_db ():
    # ~ """create database if it does not exists,
    # ~ connect to it and use
    # ~ """
    # ~ pass

# ------------------------------------ scan_folders

def scan_folders ():
    """make main job: scan multiple folders"""
    for folder in flist:
        print (f"\nscanning {folder}")
        p = Path(folder)
#        print (f"path = {p}", end=" - ")
        proc_obj (p)

# ------------------------------------ proc_obj

def proc_obj (p):
    """process any object"""
    if p.exists ():
        print (f"{p} exists")
        if p.samefile (".") or p.samefile (".."):
            return
        if p.is_dir ():
            proc_folder (p)
        else:
            proc_file (p)
    else:
        print ("not esists")

# ------------------------------------ proc_folder

def proc_folder (p):
    """process folder"""
    print (f"{p} is folder")
    obj_add ('folder', p)
    for child in p.iterdir ():
        proc_obj (child)

# ------------------------------------ proc_file

def proc_file (p):
    """process simple file"""
    print (f"{p} is simple file")
    obj_add ('file', p)

# ------------------------------------ add

def obj_add (tipa, p):
    """add object to list or db"""
    global res
    print (f"adding {p} as {tipa}")
    res += [(tipa, p.parent, p.name, p.stat().st_size, p.stat().st_mtime)]

# ------------------------------------ print_result

def print_result ():
    """print result from renewed database in pleasant way"""
    global res
    res.sort (key=lambda k: (k[0], k[3], k[4]))
    pprint (res)

    print ("\nResults:")
    was = ("", "", "", 0, 0)
    for fr in res:
        if (was[0], was[3], was[4]) == (fr[0], fr[3], fr[4]):
            w1 = was[1] / was[2]
            w2 = fr[1] / fr[2]
            print (f"file {was[0]} {w1} equals {fr[0]} {w2}")
        was = fr

    print ("\nOK.")

# ------------------------------------ main

def main ():
    """starter"""
    print ("This is HiLy project: Highly Likely folders scanner.\n")
    if good_config ():
#        init_db ()
        scan_folders ()
        print_result ()

# ------------------------------------ init

if __name__ == "__main__":
    main ()

# ------------------------------------ the end.

# NOTES:

# note: PEP8 change: function names are space separated from parameters lists even when they are empty; it is a test to see if it works better than traditional spacing.
# note: do not forget to process 3+ equivalents
