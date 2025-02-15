#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-long-substr.py 2024-03-27 2024-06-10 1.1

def solve(arr):
    """
    Finds the length of the longest common prefix among all strings in the given list.

    Args:
        arr (List[str]): A list of strings.

    Returns:
        int: The length of the longest common prefix, or 0 if there is no common prefix.
    """

    wlen = min([len(w) for w in arr])
    mlen = 0

    for pos in range(wlen):
        for wnum in range(1, len(arr)):
            if arr[0][pos] != arr[wnum][pos]:
                return pos

    return wlen


def test(loi):
    """print it and run test"""

    print(f"{loi=} => {solve(loi)}")


test(['дог', 'домен', 'домра', 'доширак'])
test(['документ', 'кот', 'кум', 'ум'])
test(['документ', 'документ', 'документ', 'документ'])

# 🖥 Задача, которую дают на собеседованиях кандидатам, которые будут работать с текстом, например в разработке поисковых систем.

# Условие:
# Дан массив со словами, в котором есть хотя бы одно слово. Необходимо найти максимально длинное общее начало каждого слова. Если такого нет — вывести пустую строку.

# Например:  имеем ['дог', 'домен', 'домра', 'доширак']. Общее начало каждого слова — 'до'.

# Другой пример: массив ['документ', 'кот', 'кум', 'ум'].
# Ответом будет пустая строка, потому что у всех этих слов нет единой общей части в начале слова.
