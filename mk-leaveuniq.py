#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-leaveuniq.py 2023-07-10 2023-07-10 1.1

from random import randint as ri

def make_list(l: int = 10) -> list[int]:
    """make list for testing"""

    arr = [ ri(0, 9) for _ in range(l)]
    arr.sort()
    return arr

# print(make_list())

def rev_dupes(l: list[int]) -> None:
    """revove duplicates"""

    llen = len(l)

    if llen == 0:
        return

    prev = None
    for ind in range(llen):
        if l[ind] == prev:
            l[ind] = None
        else:
            prev = l[ind]

    while None in l:
        l.remove(None)

def print_rem(l: list[int]) -> None:
    """only print, not make / modify array"""

    prev = None
    for e in l:
        if e != prev:
            print(e, end=", ")
            prev = e

    print()

def test():
    """run 1 test"""

    arr = make_list()
    # arr = [0, 1, 1, 2]
    print(arr)
    print_rem(arr)
    rev_dupes(arr)
    print(arr)

test()

# Задача C. Удаление дубликатов

# Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
# Правильный алгоритм последовательно обрабатывает элементы массива, сравнивая их с последним выведенным. Нужно не забыть обновлять переменную, содержащую последний выведенный элемент и, кроме того, не ошибиться при обработке последнего элемента.

# При решении этой задачи также не нужно использовать дополнительную память.
