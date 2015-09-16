#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mikhail (myke) Kolodin, 2015
# mk-rebus.py 2015-03-24 2015-03-25 1.2
# solving letter tasks
#~ [T] буквоцифровые задачи,
#~ одинаковыми буквам зашифрованы одинаковые цифры, разными - разные,
#~ найти соответствие

import string, itertools, re

# ---------------------------------
task1 = (
"F + F = N",
"2 * a = b",
"ТИК + ТАК = АКТ",
"ОН + ОНА = ОНИ",
"а+да+еда+беда=8888",
"(a+c)*(a-c)=ee"
)
task2 = (
"КЕ + НГ = УРУ",
"УДАР + УДАР = ДРАКА",
"НИТКА + НИТКА = ТКАНЬ",
"НАУКА + УЧЁБА = РАБОТА"
)
task3 = (
"FOUR + FIVE = NINE",
"MOON + MEN + CAN = REACH"
)
task4 = (
"ТРИ + ДВА = ПЯТЬ",
"НАУКА + УЧЕБА = РАБОТА",
"СИНИЦА + СИНИЦА = ПТИЧКИ",
"РАЙОН + РАЙОН = ГОРОД",
"2 * РАЙОН = ГОРОД",
"ДРАМА + ДРАМА = ТЕАТР",
"БАРБОС + БОБИК = СОБАКИ",
"ДЕТАЛЬ + ДЕТАЛЬ = ИЗДЕЛИЕ",
"КОШКА + КОШКА + КОШКА = СОБАКА",
"АИСТ + АИСТ + АИСТ + АИСТ = СТАЯ",
"ПАРУС + ПАРУС + ПАРУС + ПАРУС = РЕГАТА",
"ОДИН + ОДИН = МНОГО"
)
task0 = (
"---++()1234567++1+++ = N",
)

tasks = task1
# ---------------------------------

dsub = {}
dsubl = 0
alets = list(string.ascii_letters)
allsols = []

def reformat (t):
    """ переформатировать - унифицировать выражение """
    global dsub, dsubl
    lets = list(string.ascii_letters)
    dsub = {'=': '-'}
    for c in t:
        if c not in " +-*/=()" and c not in string.digits and c not in dsub:
            dsub [c] = lets.pop(0)
    s = ""
    for c in t:
        s += dsub.get (c, c)
    dsubl = len(dsub)
    return s

def proba (t, suba):
    """ проверяем 1 подстановку """
    global dsub, dsubl, allsols
    ll = alets[:dsubl]
    s = t
    for z in zip(ll, suba):
        s = re.sub (z[0], z[1], s)
    sz = re.sub (r"^0(\d+)", r"\1", s)
    sz = re.sub (r"\D0(\d+)", r"\1", sz)
    try:
        e = eval(sz)
    except:
        #~ print ("\nbad expression!\n")
        return 0
    ss = minus(s)
    if e == 0 and ss not in allsols:
        allsols += [ss]
        print ("good: ", ss)
        return 1
    return 0

def proc(t):
    """ обработать 1 задание """
    global dsub, dsubl, allsols, rept
    sols = 0
    allsols = []
    print ("\n=========================\n\ntask:", t, "\n")
    tn  = reformat (t)
    ll = alets[:dsubl]
    for suba in itertools.permutations("0123456789", dsubl):
        sols += proba (tn, suba)
    print ("\nfound solutions: ", sols)
    print ("\nall solutions: ", allsols, "\n")

def minus (s):
    """ заменить последний минус на равенство """
    q = s.rsplit ('-', 1)
    return q[0] + '=' + q[1]

def main():
    """ диспетчер """
    for task in tasks:
        proc(task)
    return 0

if __name__ == '__main__':
    main()

#~ =========================
#~
#~ task: F + F = N
#~
#~ good:  1 + 1 = 2
#~ good:  2 + 2 = 4
#~ good:  3 + 3 = 6
#~ good:  4 + 4 = 8
#~
#~ found solutions:  4
#~
#~ all solutions:  ['1 + 1 = 2', '2 + 2 = 4', '3 + 3 = 6', '4 + 4 = 8']
#~
#~
#~ =========================
#~
#~ task: 2 * a = b
#~
#~ good:  2 * 1 = 2
#~ good:  2 * 2 = 4
#~ good:  2 * 3 = 6
#~ good:  2 * 4 = 8
#~
#~ found solutions:  4
#~
#~ all solutions:  ['2 * 1 = 2', '2 * 2 = 4', '2 * 3 = 6', '2 * 4 = 8']
#~
#~
#~ =========================
#~
#~ task: ТИК + ТАК = АКТ
#~
#~ good:  216 + 246 = 462
#~ good:  261 + 251 = 512
#~ good:  432 + 492 = 924
#~
#~ found solutions:  3
#~
#~ all solutions:  ['216 + 246 = 462', '261 + 251 = 512', '432 + 492 = 924']
#~
#~
#~ =========================
#~
#~ task: ОН + ОНА = ОНИ
#~
#~ good:  01 + 012 = 013
#~ good:  01 + 013 = 014
#~ good:  01 + 014 = 015
#~ good:  01 + 015 = 016
#~ good:  01 + 016 = 017
#~ good:  01 + 017 = 018
#~ good:  01 + 018 = 019
#~ good:  02 + 021 = 023
#~ good:  02 + 023 = 025
#~ good:  02 + 024 = 026
#~ good:  02 + 025 = 027
#~ good:  02 + 026 = 028
#~ good:  02 + 027 = 029
#~ good:  03 + 031 = 034
#~ good:  03 + 032 = 035
#~ good:  03 + 034 = 037
#~ good:  03 + 035 = 038
#~ good:  03 + 036 = 039
#~ good:  04 + 041 = 045
#~ good:  04 + 042 = 046
#~ good:  04 + 043 = 047
#~ good:  04 + 045 = 049
#~ good:  05 + 051 = 056
#~ good:  05 + 052 = 057
#~ good:  05 + 053 = 058
#~ good:  05 + 054 = 059
#~ good:  06 + 061 = 067
#~ good:  06 + 062 = 068
#~ good:  06 + 063 = 069
#~ good:  07 + 071 = 078
#~ good:  07 + 072 = 079
#~ good:  08 + 081 = 089
#~
#~ found solutions:  32
#~
#~ all solutions:  ['01 + 012 = 013', '01 + 013 = 014', '01 + 014 = 015', '01 + 015 = 016', '01 + 016 = 017', '01 + 017 = 018', '01 + 018 = 019', '02 + 021 = 023', '02 + 023 = 025', '02 + 024 = 026', '02 + 025 = 027', '02 + 026 = 028', '02 + 027 = 029', '03 + 031 = 034', '03 + 032 = 035', '03 + 034 = 037', '03 + 035 = 038', '03 + 036 = 039', '04 + 041 = 045', '04 + 042 = 046', '04 + 043 = 047', '04 + 045 = 049', '05 + 051 = 056', '05 + 052 = 057', '05 + 053 = 058', '05 + 054 = 059', '06 + 061 = 067', '06 + 062 = 068', '06 + 063 = 069', '07 + 071 = 078', '07 + 072 = 079', '08 + 081 = 089']
#~
#~
#~ =========================
#~
#~ task: а+да+еда+беда=8888
#~
#~ good:  7+27+427+8427=8888
#~
#~ found solutions:  1
#~
#~ all solutions:  ['7+27+427+8427=8888']
#~
#~ =========================
#~
#~ task: (a+c)*(a-c)=ee
#~
#~ good:  (6+5)*(6-5)=11
#~ good:  (7+4)*(7-4)=33
#~ good:  (8+3)*(8-3)=55
#~ good:  (9+2)*(9-2)=77
#~
#~ found solutions:  4
#~
#~ all solutions:  ['(6+5)*(6-5)=11', '(7+4)*(7-4)=33', '(8+3)*(8-3)=55', '(9+2)*(9-2)=77']

