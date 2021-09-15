#!/usr/bin/env python3

# myke 2021-09-15
# найти все числа 0 .. upto [100], у которых сумма цифр равна их произведению

#from myke import sumprod, sumprodold, sumprodsimple

# ------------------------------
# версия для новичков

def sumprodold(upto=100):
  """ найти все числа 0 .. upto,
  у которых сумма цифр равна их произведению
  """
  for i in range(upto):
    if osum(i) == oprod(i):
      print(i, end=", ")

def osum(num):
  """ другая сумма цифр числа"""
  summa = 0
  stroka = str(num)
  for bukva in stroka:
    summa += int(bukva)
  return summa

def oprod(num):
  """ другое произведение цифр числа"""
  prod = 1
  stroka = str(num)
  for bukva in stroka:
    prod *= int(bukva)
  return prod

# ------------------------------
# версия профи :)

from functools import reduce

def sumprod(upto : int = 100):
  """ найти все числа 0 .. upto,
  у которых сумма цифр равна их произведению
  """
  for i in range(upto):
    if mysum(i) == myprod(i):
      print(i, end=", ")

def mysum(num : int) -> int:
  """ сумма цифр числа"""
  return reduce(lambda x, y: x+y, [int(x) for x in str(num)], 0)

def myprod(num : int) -> int:
  """ произведение цифр числа"""
  return reduce(lambda x, y: x*y, [int(x) for x in str(num)], 1)

# 1_000_000: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 123, 132, 213, 231, 312, 321, 1124, 1142, 1214, 1241, 1412, 1421, 2114, 2141, 2411, 4112, 4121, 4211, 11125, 11133, 11152, 11215, 11222, 11251, 11313, 11331, 11512, 11521, 12115, 12122, 12151, 12212, 12221, 12511, 13113, 13131, 13311, 15112, 15121, 15211, 21115, 21122, 21151, 21212, 21221, 21511, 22112, 22121, 22211, 25111, 31113, 31131, 31311, 33111, 51112, 51121, 51211, 52111, 111126, 111162, 111216, 111261, 111612, 111621, 112116, 112161, 112611, 116112, 116121, 116211, 121116, 121161, 121611, 126111, 161112, 161121, 161211, 162111, 211116, 211161, 211611, 216111, 261111, 611112, 611121, 611211, 612111, 621111,

# https://codecamp.ru/blog/map-filter-reduce/
# Что такое Map, Filter и Reduce в Python? Это функциональное программирование? (2020

# ------------------------------
# как надо было: :)

def sumprodsimple():
  for i in range(10):
    for j in range(10):
      if i+j == i*j or i == 0:
        print(i*10+j)

# ---------------------------------------

def main():

    #sumprodold()
    #sumprodold(1000)

    #sumprod()
    #sumprod(1000)

    sumprodsimple()

main()
