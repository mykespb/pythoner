#!/usr/bin/env python3
# Mikhail Kolodin
# primes Eratosphen-1
# 2022-06-09 2022-06-11 1.1

def erato1(limit=1000):
    """таблица простых чисел, решето Эратосфена, некомпактно"""

    primes = [0 for _ in range(limit)]
    primes[0] = primes[1] = -1
    for num in range(2, limit):
        if primes[num] == 0:
            primes[num] = 1
            print(num, end=", ")
            for out in range(num+num, limit, num):
                primes[out] = -1

# erato1()

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,

# ~ def up(n):
    # ~ """взведение бита числа"""
    # ~ global primes
    # ~ nbyte = n // size
    # ~ nbit  = n % size
    # ~ nbyte, nbit = divmod(n, SIZE)
    # ~ primes[nbyte] |= (1 << nbit)


SIZE = 8


def init(limit):
    """инициализация масива"""
    global primes
    primes = [255 for _ in range(limit // SIZE + 1)]
    down(0)
    down(1)


def down(n):
    """сброс бита числа"""
    global primes
    # ~ nbyte = n // SIZE
    # ~ nbit  = n % SIZE
    nbyte, nbit = divmod(n, SIZE)
    primes[nbyte] &= ~(1 << nbit)


def isup(n):
    """проверка бита числа"""
    # ~ nbyte = n // SIZE
    # ~ nbit  = n % SIZE
    nbyte, nbit = divmod(n, SIZE)
    return primes[nbyte] & (1 << nbit)


def erato2(limit=1000):
    """таблица простых чисел, решето Эратосфена, компактно"""
    init(limit)
    for num in range(2, limit):
        if isup(num):
            print(num, end=", ")
            for out in range(num+num, limit, num):
                down(out)


erato2()
