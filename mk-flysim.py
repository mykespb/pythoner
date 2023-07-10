#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-flysim.py 2023-07-10 2023-07-10 1.0
# задача о мухе, моделирование

def run():

    # всё - в м, с, м/с
    # скорость мухи
    v_fly = 100_000 / 3600.

    # скорость поездов
    v_train = 50_000 / 3600.

    # расстояние исходное
    dist = 300_000

    # путь мухи
    path = 0.

    # начальные положения
    fly_at = 0.
    left_at = 0.
    right_at = 300_000.

    # сколько разворотов сделано
    turns = 0

    dir = 1
    while dir:

        if dir > 0:
            # fly right
            fly_at += v_fly
            left_at += v_train
            right_at -= v_train
            path += v_fly

            if left_at > right_at:
                break

            if fly_at > right_at:
                print(f"{turns=}, {path=}")              
                dir = -1
                turns += 1

        if dir < 0:
            # fly right
            fly_at -= v_fly
            left_at += v_train
            right_at -= v_train
            path += v_fly

            if left_at > right_at:
                break

            if fly_at < left_at:
                print(f"{turns=}, {path=}")              
                dir = -1
                turns += 1

    print(f"\nfinally: {path=}")              

run()

# ... 
# turns=1196, path=299916.6666666578
# turns=1197, path=299944.44444443553
# turns=1198, path=299972.2222222133
# turns=1199, path=299999.99999999104

# finally: path=300027.7777777688
