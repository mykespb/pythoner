#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 2014-04-15 2016-01-29 5.1.0. simpel test
# 2016-02-11 6.1.0 testfor v.3

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
