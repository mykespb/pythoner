#!/usr/bin/env python
# -*- coding: utf-8 -*-

# shof.py
# (C) Mikhail (myke) Kolodin, 2021
# прячем файлы для отправки на работу и обратно

# 2021-12-27 2021-12-28 3.2

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
version = '3.2'

# главный пакофайл
shof    = "shof.shof"

# список возможных запускателей
allshof = "shof.shof shof.py shof.sh shof".split()

# обрабатываемые в данной версии расширения
exts    = "sh py pl".split()

# обработчики -- см. в конце файла

# )))конец настроек

dt = datetime.datetime.now()
cwd = os.getcwd()
sysdir = tuple('bin boot sbin root dev etc srv media mnt opt usr var proc run sys snap timeshift'.split())

if cwd.endswith(sysdir):
    print("cannot run in bin or system directory!")
    exit(1)

todos = []

def pack():
    """
    упаковка
    """
    global todos
    
    print("do packing\ndirectory", os.getcwd(), "\nat", dt)

    if os.path.isfile(shof):
        os.remove(shof)

    # список файлов
    files = os.listdir(".")
    print("files:", files)

    todo  = []
    todos = []
    for afile in files:
        if os.path.isfile(afile) and afile not in allshof:
            todo.append(afile)

    print("files to process:", todo)

    # по всем известным опасным файлам
    for afile in todo:
        print("processing:", afile)
        for ext, proc in packers.items():
            if afile.endswith(ext):
                proc(afile)
                break
        else:
            todos.append(afile)

    # упаковываем в архив и переименовываем
    zf = zipfile.ZipFile(shof, 'w')
    for afile in todos:

        try:
            print("adding", afile, "to archive...", end="")
            zf.write(afile)
            print("ok.")
        except:
            print("failed.")

        # ~ print("removing", afile, end="...")
        # ~ try:
            # ~ os.remove(afile)
            # ~ print("done.")
        # ~ except:
            # ~ print("failed.")
        
    zf.close()

    # удаляем исходные файлы
    allfiles = todos[:]
    allfiles.extend(todos)
    allfiles = list(set(allfiles))
    print("deleting files:", allfiles)
    for afile in allfiles:
        try:
            print("delete:", afile, end=" ")
            os.remove(afile)
            print("ok.")
        except:
            print("failed.")
    

def pack_python(fn):
    """
    упаковка питоновского файла
    """
    global todos
    
    of = fn + '.shof'

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("#!", "(SHOF_SHEBANG)")
                .replace("python", "(SHOF_LANG)")
                )
            ouf.write(line)

    os.remove(fn)
    todos.append(of)


def pack_perl(fn):
    """
    упаковка перлового файла
    """
    global todos
    
    of = fn + '.shof'

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("#!", "(SHOF_SHEBANG)")
                .replace("perl", "(SHOF_LANG)")
                )
            ouf.write(line)

    os.remove(fn)
    todos.append(of)


def pack_bash(fn):
    """
    упаковка bash файла
    """
    global todos
    
    of = fn + '.shof'

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("#!", "(SHOF_SHEBANG)")
                .replace("bash", "(SHOF_LANG_BASH)")
                )
            ouf.write(line)

    os.remove(fn)
    todos.append(of)


def unpack():
    """
    распаковка
    """
    print("do unpacking\ndirectory", os.getcwd(), "\nat", dt)

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

        files = os.listdir(".")
        print("files:", files)

        todo  = []
        for afile in files:
            if os.path.isfile(afile) and afile not in allshof:
                todo.append(afile)

        print("files to process:", todo)

        # по всем известным опасным файлам
        for afile in todo:
            try:
                print("processing:", afile)
                for ext, proc in unpackers.items():
                    if afile.endswith(ext):
                        proc(afile)
                        break
            except:
                print("bad file", afile)

    except:
        print("cannot process archive", shof)


def unpack_python(fn):
    """
    распаковка питоновского файла
    """
    of = fn[:-5]
    print("unpacking python file", fn, "to", of)

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("(SHOF_SHEBANG)", "#!")
                .replace("(SHOF_LANG)", "python")
                )
            ouf.write(line)

    print("removing", fn, end="...")
    os.remove("./" + fn)
    print("done")


def unpack_perl(fn):
    """
    распаковка перлового файла
    """
    of = fn[:-5]
    print("unpacking perl file", fn, "to", of)

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("(SHOF_SHEBANG)", "#!")
                .replace("(SHOF_LANG)", "perl")
                )
            ouf.write(line)

    print("removing", fn, end="...")
    os.remove("./" + fn)
    print("done")


def unpack_bash(fn):
    """
    распаковка bash файла
    """
    of = fn[:-5]
    print("unpacking perl file", fn, "to", of)

    with open(fn) as inf, open(of, 'w') as ouf:
        for line in inf:
            line = (line
                .replace("(SHOF_SHEBANG)", "#!")
                .replace("(SHOF_LANG_BASH)", "bash")
                )
            ouf.write(line)

    print("removing", fn, end="...")
    os.remove("./" + fn)
    print("done")


def main():
    print('This is SHOF {} by myke to facilitate files exchange.' .format(version))
    if os.path.exists(shof):
        unpack()
    else:
        pack()
    print('SHOF done.')

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
# ~ ver. 2.0. готово для питоновских и прочих неопасных.
# ~ ver. 3.0. готово для всех файлов.

# ================================================
