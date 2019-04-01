# -*- coding: utf-8 -*-
# by tunan
# download: https://github.com/tunan66666/python3

import xlwt, os

def create_excel(file_name, data_list):
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet')
    row = 0
    for data in data_list:
        col = 0
        for d in data:
            sheet.write(row, col, d)
            col += 1
        row += 1
    f_path = os.getcwd()
    file_path = '%s/data/%s' %(f_path, file_name)
    book.save(file_path)

file_name = 'create_excel.xls'
data_list = [['id', 'name']]
list1 = ['1', 'a']
list2 = ['1', 'b']
list3 = ['1', 'c']
data_list.append(list1)
data_list.append(list2)
data_list.append(list3)

create_excel(file_name, data_list)
print('create excel success')

