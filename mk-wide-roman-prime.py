#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2016-03-26 1.1

#  https://habrahabr.ru/post/280179/
# Самое широкое простое число, записанное римскими цифрами
# Один из моих любимых развлекательных твиттеров – это @wacnt. Там появляются вопросы, на которые не может ответить математический поисковик Wolfram|Alpha. На некоторые, кстати, мне сумел дать ответ виртуальный ассистент Facebook M.
#
# Вот штучка из недавних, которая заставила меня улыбнуться:
# простое число, не большее 4000, получающееся самым широким при записи римскими цифрами шрифтом Times New Roman

# решаем пока без шрифта

MAX = 4000

primes = [2]

def makeprimes():
    """ список простых чисел до MAX """
    global primes

    for tested in range(3, MAX+1):
        for tester in primes:
            if tested % tester == 0:
                break
        else:
            primes += [tested]

    print ("primes=", primes)


def roman(i):
    """ перевести число из арабской записи в римскую """
    out = ""
    if i == 0: return "0"
    if i < 0:
        i = -i
        out = "-"

    # IVXLCDM
    para = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

    while i > 0:
        for p in para:
            if i >= p[0]:
                i -= p[0]
                out += p[1]
                break

    return out


def makeromans ():
    """ перебор и выбор длиннейшего с печатью """
    maxri = 0
    maxlri = 1

    for i in primes:
        ri = roman(i)
        lri = len(ri)
        yes = ""
        if lri > maxlri:
            maxlri = lri
            maxri = ri
            yes = "yes!"
        print (i, ri, lri, yes)

    print ("\nрезультат: длиннейшее римское число {} с длиной {}" .format(maxri, maxlri))

    return 0

def main(args):
    """ перебор и выбор длиннейшего с печатью """

    makeprimes()
    makeromans()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


# ...
#~ 3863 MMMDCCCLXIII 12
#~ 3877 MMMDCCCLXXVII 13
#~ 3881 MMMDCCCLXXXI 12
#~ 3889 MMMDCCCLXXXIX 13
#~ 3907 MMMCMVII 8
#~ 3911 MMMCMXI 7
#~ 3917 MMMCMXVII 9
#~ 3919 MMMCMXIX 8
#~ 3923 MMMCMXXIII 10
#~ 3929 MMMCMXXIX 9
#~ 3931 MMMCMXXXI 9
#~ 3943 MMMCMXLIII 10
#~ 3947 MMMCMXLVII 10
#~ 3967 MMMCMLXVII 10
#~ 3989 MMMCMLXXXIX 11

#~ результат: длиннейшее римское число MMDCCCLXXXVII с длиной 13

