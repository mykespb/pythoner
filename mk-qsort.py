#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# quicksort

import random

def qsort(L):
    if L: return qsort([x for x in L[1:] if x<L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
    return []

for i in range(5):
    a = [random.randint (1, 100) for j in range (10)]
    print ("\nfrom:", a)
    a = qsort(a)
    print ("to:  ", a)
