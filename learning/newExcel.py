# -*- encoding: UTF-8 -*-

import xlwt

title = ['姓名','年龄','性别','分数']
stus = [['mary','20','女','89.9'],['mary','20','女','89.9'],['mary','20','女','89.9'],['mary','20','女','89.9']]
#新建一个excel对象
wbk = xlwt.Workbook()
#添加一个名为课程表的sheet页
sheet = wbk.add_sheet('stu')
for i in range(len(title)):
    sheet.write(0,i,title[i])
for i in range(len(stus)):
    if i != 0:
        for j in range(4):
            sheet.write(i,j,stus[i][j])
wbk.save('szz.xls')