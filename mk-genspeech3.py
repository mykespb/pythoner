#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# mk-genspeech3.py
# py2 2014-05-25 2017-04-22 1.2 
# py3 2021-12-26 2021-12-26 2.1 
# Генератор речей

import random

text = """
  Товарищи! / Господа! / Коллеги! / Дорогие товарищи! / Уважаемые коллеги! / Дамы и господа! /  Уважаемые участники! / / / / / / / / / /
  С другой стороны / Равным образом / Не следует, однако, забывать о том, что /  Таким образом / Повседневная практика показывает, что / Значимость этих проблем настолько очевидна, что / Из выступления товарища начальника ясно следует, что / В решениях съезда нашей партии указано, что/ Разнообразный и богатый опыт показывает, что / Задача организации, в особенности же / Идейные соображения  высшего порядка, а также / Принимая во внимание, что / Вы, конечно, знаете, что / Вам, должно быть, известен тот факт, что
  реализация намеченных плановых заданий / рамки и место обучения кадров / постоянный количественный рост и сфера нашей активности / сложившаяся структура организации / новая модель организационной деятельности / дальнейшее развитие различных форм деятельности / постоянное информационно-пропагандистское обеспечение нашей деятельности / управление и развитие структуры / консультация с широким активом / начало повседневной работы по формированию позиции
  играет важную роль в формировании / требуют от нас анализа / требуют определения и уточнения /  способствуют подготовке и реализации / обеспечивают широкому кругу специалистов участие в формировании
  , что позволяет выполнить важные задания по разработке / , что в значительной степени обуславливает создание / , что позволяет оценить значение / , что представляет собой интересный эксперимент / , что влечёт за собой интересный процесс внедрения и модернизации
  существенных финансовых и административных условий / дальнейших направлений развития /  системы массового участия / позиций, занимаемых участниками в отношении поставленных задач /  новых предложений / направлений прогрессивного развития / форм воздействия /  модели развития / соответствующих условий активизации / системы обучения кадров, соответствующей  насущным потребностям
  """

def make_speech (rows=1):
    parts = [part.split('/') for part in text.split('\n')]
    for num in range(1, rows+1):
        print ("Пункт %d.\n" % num + "".join([random.choice(part) for part in parts]) + '.')

make_speech(4)

# ~ Пункт 1.
  # ~ Уважаемые участники!  Задача организации, в особенности же  новая модель организационной деятельности  обеспечивают широкому кругу специалистов участие в формировании , что в значительной степени обуславливает создание   новых предложений   .
# ~ Пункт 2.
 # ~ Принимая во внимание, что  новая модель организационной деятельности   играет важную роль в формировании  , что в значительной степени обуславливает создание  дальнейших направлений развития   .
# ~ Пункт 3.
  # ~ Значимость этих проблем настолько очевидна, что  рамки и место обучения кадров  требуют от нас анализа  , что влечёт за собой интересный процесс внедрения и модернизации позиций, занимаемых участниками в отношении поставленных задач   .
# ~ Пункт 4.
 # ~ Идейные соображения  высшего порядка, а также   реализация намеченных плановых заданий   способствуют подготовке и реализации  , что представляет собой интересный эксперимент   модели развития   .