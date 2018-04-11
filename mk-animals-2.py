#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ssyp42/ mk-animals-1.py 2017-03-03 2.1
# игра в животных, версия 2, простой цикл без отладки

import pprint

def main():
    """ диспетчер """
    global B

    print (f"Привет. Это игра в животных")

    B = {}
    while sess() and (input("\nПродолжаем? (да/нет) ")[0] == "д"): pass

    return 0

def sess ():
    """ сессия вопросов-ответов"""
    global B
    E = B

    print ("\nИграем.\nВы всегда можете остановить игру, введя точку (.)\n")

    while E:
        print (f"Вопрос: {E['quest']}? ")

        rep = input()
        if rep[0] == ".":
            return False

        if rep[0] == "д":
            repn = input(f"Это {E['name']}? ")

            if repn[0] == "д":
                print (f"\nУра! Угадал! Это {E['name']}!\n")
                return True

            else:
                if E['yes']:
                    E = E['yes']
                    continue
                else:
                    name = input ("Да уж. Не знаю зверя. Сдаюсь. Как он называется?  ")
                    quest = input ("Каким вопросом его можно определить?  ")
                    N = {}
                    N["name"]  = name
                    N["quest"] = quest
                    N['yes']   = {}
                    N['no']    = {}
                    E['yes']   = N
                    break

        if E['no']:
            E = E['no']
            continue
        else:
            name = input ("Нет уж. Не знаю зверя. Сдаюсь. Как он называется?  ")
            quest = input ("Каким вопросом его можно определить?  ")
            N = {}
            N["name"]  = name
            N["quest"] = quest
            N['yes']   = {}
            N['no']    = {}
            E['no']    = N
            break

    else:
        name = input ("Не знаю пока зверей. Сдаюсь. Как этот называется?  ")
        quest = input ("Каким вопросом его можно определить?  ")
        N = {}
        N["name"]  = name
        N["quest"] = quest
        N['yes']   = {}
        N['no']    = {}
        B          = N

    return True

if __name__ == '__main__':
    main()
