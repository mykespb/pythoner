#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# 2014-04-15 2016-01-29 5.1. simpel test

#from __future__ import division, print_function
#import sqlite3 as sql
#import datetime
#import os
#import re

from bottle import *

@get('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000)
#    run(host='localhost', port=8080)

#~ @get('/index')
