#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  foobar.py 1.2
#  Write a program that prints the numbers from 1 to 100. But for multiples of three print “Foo” instead of the number and for the multiples of five print “Bar”. For numbers which are multiples of both three and five print “FooBar”.

def main():

    for n in range(1, 101):
        print (
            "FooBar" if n%15 == 0 else
            "Foo" if n%3 == 0 else
            "Bar" if n%5 == 0 else n
            , ", ",
            end="\n" if n%10 == 0 else "")

    return 0

if __name__ == '__main__':
    main()
