#!python

# (C) Mihail Kolodin, 2021
# offmaker.py 2021-10-03 2021-10-03 0.1

# обработка вордовых шаблонов и эксельных списков
# с получением вордовых писем в отдельных файлах

# ~ import xlrd
import openpyxl
from docx import Document

template  = "template.docx"
lopersons = "lopersons.xlsx"
outdir    = "outdir"

print ("here we start with {} as template and {} as list of persons\nresult files will be written to {} directory".format
    (template, lopersons, outdir))

wb = openpyxl.load_workbook (lopersons)
sheet = wb.active
print (sheet)

print("Rows: {}, columns: {}" . format(smr := sheet.max_row, smc := sheet.max_column))
cols = []
for item in sheet.iter_cols(0, smc):
    cols.append(item[0].value)
print(cols)

for i, row in enumerate (sheet.iter_rows (values_only = True)):
    if i == 0:
        continue

    print ("-------------------------------\nline {}" .format(i))
    for j in range(smc):
        print ("data {} is {}" .format(cols[j], row[j]))

doc = Document(template)

print (doc.paragraphs)

# useful links:

# https://www.marsja.se/your-guide-to-reading-excel-xlsx-files-in-python/
# Your Guide to Reading Excel (xlsx) Files in Python
# by Erik Marsja | Feb 16, 2020 | Programming, Python
