#!/usr/bin/env python3
# mk-dbook.py (C) Mikhail Kolodin, 2018
# 1.1 2018-02-21 2018-02-27

# create daybook file with given [month [year]]
# with current date as default

import sys, datetime, os.path, calendar

ver = "1.1 of 2018-02-27"

today = datetime.date.today()
year = today.year
month = today.month

names = "январь февраль март апрель май июнь июль август сентябрь октябрь ноябрь декабрь".split()
wdps = "вс пн вт ср чт пт сб вс".split()

def help():
    print ("""
Usage:
mk-dbook.py -h          get this help
mk-dbook.py --help      get this help
mk-dbook.py             make daybook for current month and year
mk-dbook.py MONTH       make daybook for given MONTH and current year
mk-dbook.py MONTH YEAR  make daybook for given MONTH and YEAR

Existing daybook will not be overwritten.
""")

def error():
    print ("Bad parameter(s). Quit.")

def make (year, month):
    print (f"called with year={year}, month={month}")
    days = 31, (29 if calendar.isleap(year) else 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
#    print ("leap:", 29 if calendar.isleap(year) else 28)
    if year < 2000 or year > today.year or month < 1 or month > 12:
        error()
        return

    fname = f"{year:04d}-{month:02d}.txt"
    print (f"filename = {fname}")
    if os.path.exists(fname):
        print (f"File {fname} already exists. No actions.")
        return

    with open (fname, "w") as fout:
        fout.write ("Дневник за %s %d\n" % (names[month-1], year))

        for day in range(1, days[month-1]+1):
#            print  (year, month, day)
            wd = calendar.weekday (year, month, day)
            wdp = wdps[wd+1]
            fout.write (f"\n---------------------------------------------------------------------\n{year:04d}-{month:02d}-{day:02d} {wdp}\n---------------------------------------------------------------------\n\n")

        fout.write ("\n\n---------------------------------------------------------------------\n\n")

def main():
    global year, month
    lensa = len(sys.argv)
    print (f"This is mk-dbook.py ver. {ver}, args: {lensa},\ntoday is: year={year}, month={month}\nA tool for making monthly daybooks.")
    if lensa > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        help()
        return
    if lensa == 1:
        make (today.year, today.month)
    elif lensa == 2:
        try:
            month = int(sys.argv[1])
            make (year, month)
        except:
            error()
    elif lensa == 3:
        try:
            month = int(sys.argv[1])
            year = int(sys.argv[2])
            make (year, month)
        except:
            error()

main()
