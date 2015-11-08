#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# testing PostgreSQL 9.4.5
# mk-pg1.py 2015-11-08 1.0
# 1. connect and select

import psycopg2
import sys

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='testdb' user='testu' password='testu'"

    # print the connection string we will use to connect
    print ("Connecting to database\n    ->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print ("Connected!\n")

main()

# https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
