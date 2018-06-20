# -*- coding: UTF-8 -*-

import xlrd
from datetime import date,datetime
import os

pdoDir = os.path.split(os.path.realpath(__file__))[0]
excelFile = os.path.join(pdoDir,"productCase.xlsx")

class excelRead():
    workbook = xlrd.open_workbook(excelFile)
    print(workbook.sheet_names())
    sheet_names = workbook.sheet_names()
    for sheet_name in sheet_names:
        sheet2 = workbook.sheet_by_name(sheet_name)
        print (sheet_name)
        rows = sheet2.row_values(3)
        cols = sheet2.col_values(2)
        print(rows)
        print(cols)
        print(sheet2.nrows)
        print(sheet2.ncols)
        for rownum in range(sheet2.nrows):
            print(sheet2.row_values(rownum))
        for clonum in range(sheet2.ncols):
            print(sheet2.col_values(clonum))

if __name__ =="__main__":
    excelRead()
