#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hily 2018-05-06 M.Kolodin
# Highly Likely Project

# ver. 0.4. it must scan folders in hily.iin and print result (same files) into file hily.out.

# note: PEP8 change: function names are separated from parameters lists even when they are empty; it is a tets to se if it works better than traditional spacing.

import sqlite3
import os.path

# ------------------------------------ config
# file with config
CONFIG = "hily.ini"

# folders list
flist = []

# outfile with pretty printed result, with default value
outfile = "./outfile.txt"

# ------------------------------------ start

def good_config ():
    """read configuration and cry if none or wrong"""

    global flist, outfile

    print ("Looking for configuration file.")

    if os.path.exists (CONFIG):
        with open (CONFIG) as config:
            for line in config:
                line = line.strip ()
                print (line)
                if len (line):
                    cmd, data = line.split ()
                    if cmd == "in":
                        flist += [data]
                    elif cmd == "out":
                        outfile = data
        print (f"\nFolders list is {flist},\nresult will be written to {outfile}.")
    else:
        print (f"Config file {CONFIG} does not exist. Quitting.")

    return True

# ------------------------------------ init_db

def init_db ():
    """create database if it does not exists,
    connect to it and use
    """
    pass

# ------------------------------------ scan_folders

def scan_folders ():
    """make main job: scan multiple folders recursively"""
    pass

# ------------------------------------ print_result

def print_result ():
    """print result from renewed database in pleasant way"""
    print ("OK.")

# ------------------------------------ main

def main ():
    """starter"""
    print ("This is HiLy project: Highly Likely folders scanner.\n")
    if good_config ():
        init_db ()
        scan_folders ()
        print_result ()

# ------------------------------------ init

if __name__ == "__main__":
    main ()

# ------------------------------------ the end.
