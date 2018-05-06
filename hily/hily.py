#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hily 2018-05-06 M.Kolodin
# Highly Likely Project

# ver. 0.1. it must scan folders in hily.iin and print result (same files) into file hily.out.

import sqlite3

def start():
    """read configuration and cry if none or wrong"""
    return True

def init_db():
    """create database if it does not exists,
    connect to it and use
    """
    pass

def scan_folders():
    """make main job: scan multiple folders recursively"""
    pass

def print_result():
    """print result from renewed database in pleasant way"""
    print ("OK.")

def main():
    """starter"""
    if start():
        init_db()
        scan_folders()
        print_result()

if __name__ == "__main__":
    main()
