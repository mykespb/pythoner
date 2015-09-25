#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-makeprodb1.py (С) М.Колодин, 2015  2015-09-23 1.2
# формирование задания для создания своей СУБД
# in: # of lines

import random, sys

names1 = "Александр Андрей Борис Василий Виктор Владимир Геннадий Егор Иван Игорь Кирилл Михаил Николай Олег Пётр Сергей Семён Тит Фёдор Яков".split()

names2 = "Алексеев Александров Борисов Васильев Викторов Владимиров Егоров Кириллов Михайлов Николаев Петров Сергеев Семёнов Титов Фёдоров Яковлев".split()

act = "покупка продажа".split()

remark = "еда одежда спорт бизнес туризм банки дом машина мобила транспорт".split()

def main():
    total = int(sys.argv[1]) if len(sys.argv)>1 else 1
    for i in range(total):
        print ("%s %s %s %.2f %s" %
            (random.choice(names2),
            random.choice(names1),
            random.choice(act),
            random.randint(0, 10000) / 100.,
            random.choice(remark)))

    return 0

main()

#~ call:
#~ ./mk-make-prodb1.py 100 > mk-make-prodb100.txt
#~ sort mk-make-prodb100.txt > mk-make-prodb100.srt
#~ ./mk-make-prodb1.py 1000 > mk-make-prodb1000.txt
#~ sort mk-make-prodb1000.txt > mk-make-prodb1000.srt
#~ ./mk-make-prodb1.py 10000 > mk-make-prodb10000.txt
#~ sort mk-make-prodb10000.txt > mk-make-prodb10000.srt
#~ ./mk-make-prodb1.py 100000 > mk-make-prodb100000.txt
#~ sort mk-make-prodb100000.txt > mk-make-prodb100000.srt
