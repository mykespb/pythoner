#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# evenfibo.py  myke 2014-06-26 2016-02-03 2.1
# calucate sum of even fido numbers < 1.000.000
# from yandex prog school
# http://tech.yandex.ru/education/prog/school/

def fiba ():
    f1, f2 = 1, 1
    yield 1
    while True:
        f1, f2 = f2, f1+f2
        yield f1

def fibb (nlim=10):
    f1, f2 = 1, 1
    for i in range(nlim):
        yield f1
        f1, f2 = f2, f1+f2

def main():
    print (list(fibb(20)))

def main2():
    fn = fiba()
    for _ in range(10):
        print (fn.next())

def main1():
    summa = 0
    f1, f2, f3 = 1, 1, 2
    lim = 1000000

    while f3 < lim:
        #~ if f3 % 2 == 0:
            #~ summa += f3
            #~ print f3, summa
        #~ else:
            #~ print f3
        summa += f3 if f3 % 2 == 0 else 0
        f1, f2, f3 = f2, f3, f2+f3

    print ("summa=", summa)
    return 0

main()

# 1089154
