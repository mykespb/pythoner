#!python

# (C) Mihail Kolodin, 2021
# offmaker.py 2021-10-03 2021-10-03 0.1

# обработка вордовых шаблонов и эксельных списков
# с получением вордовых писем в отдельных файлах

# ~ import xlrd
import openpyxl

template  = "template.docx"
lopersons = "lopersons.xlsx"
outdir    = "outdir"

print ("here we start with {} as template and {} as list of persons\nresult files will be written to {} directory".format
    (template, lopersons, outdir))

with open (template) as ftpl:
    print ("file '{}' is open" . format (template))

    # ~ wb = xlrd.open_workbook(lopersons)
    # ~ sheet = wb.shhet_by_index(0)
    # ~ sheet.cell_value(0, 0)
    # ~ print (sheet.ncols)

    wb = openpyxl.load_workbook (lopersons)
    sheet = wb.active
    print (sheet)

    print("Rows: {}, columns: {}" . format(smr := sheet.max_row, smc := sheet.max_column))
    cols = []
    for item in sheet.iter_cols(0, smc):
        cols.append(item[0].value)
    print(cols)
