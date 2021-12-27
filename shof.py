#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# shof.py
# (C) Mikhail (myke) Kolodin, 2021
# прячем файлы для отправки на работу и обратно

# 2021-12-27 2021-12-27 1.0

# вызов:
# упаковка:
#   shof.py
#   на выходе - файл shof.shof,
#   пригодный для отправки по почте,
#   исходные файлы удаляются,
#   подкаталоги не используются,
#   все обработанные файлы получают .shof в конце имени
# распаковка: 
#   в каталоге с файлом shof.shof сказали
#   shof.py
#   на выходе - всё, что там в архиве было
#   исходный файл удаляется
# shof, shof.sh, shof.shof - не трогаются

import os, os.path, datetime, zipfile

# (((настройки

# текущая версия
version = '0.1'

# главный пакофайл
shof    = "shof.shof"

# список возможных запускателей
allshof = "shof.shof shof.py shof.sh shof".split()

# обрабатываемые в данной версии расширения
exts    = "sh py pl".split()

# обработчики -- см. в конце файла

# )))конец настроек

dt = datetime.datetime.now()


def pack():
    """
    упаковка
    """
    print("SHOF: do packing\ndirectory", os.getcwd(), "\nat", dt)

    # список файлов
    files = os.listdir(".")
    print("files:", files)

    todo = []
    for afile in files:
        if os.path.isfile(afile) and afile not in allshof:
            todo.append(afile)

    print("SHOF: files to process:", todo)

    # по всем известным опасным файлам
    for afile in todo:
        print("processing:", afile)
        for ext, proc in packers.items():
            if afile.endswith(ext):
                proc(afile)

    # упаковываем в архив и переименовываем
    zf = zipfile.ZipFile(shof, 'w')
    for afile in todo:
        zf.write(afile)
    zf.close()

    # удаляем исходные файлы
    print("deleting files:", todo)
    for afile in todo:
        try:
            print(afile, end=" ")
            os.remove(afile)
            print("ok")
        except:
            print("fail")
    

def pack_python(fn):
    """
    упаковка питоновского файла
    """
    ...


def pack_perl(fn):
    """
    упаковка перлового файла
    """
    ...


def pack_bash(fn):
    """
    упаковка bash файла
    """
    ...


def unpack():
    """
    распаковка
    """
    print("do unpack in", os.getcwd())
    
    # распаковываем
    try:
        zf = zipfile.ZipFile(shof, 'r')

        # по каждому из известных опасных файлов - делаем рабочими
        zf.extractall()
        zf.close()
        print("archive", shof, "extracted", end=" ")

        # удаляем исходный главный файл
        os.remove(shof)
        print("and removed")

    except:
        print("cannot procerss archive", shof)


def unpack_python(fn):
    """
    распаковка питоновского файла
    """
    ...


def unpack_perl(fn):
    """
    распаковка перлового файла
    """
    ...


def unpack_bash(fn):
    """
    распаковка bash файла
    """
    ...


def main():
    if os.path.exists(shof):
        unpack()
    else:
        pack()

# конец настроек -- упаковщики и распаковщики

packers = {
    ".py": pack_python,
    ".pl": pack_perl,
    ".sh": pack_bash
    }

unpackers = {
    ".py.shof": unpack_python,
    ".pl.shof": unpack_perl,
    ".sh.shof": unpack_bash
    }


if __name__ == '__main__':
    main()

# ================================================

# ~ ver. 1.0. готово создание архива и распаковка,
# ~ пока без обработки внутренностей "опасных" файлов
