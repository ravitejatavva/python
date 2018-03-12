'''
To unload data from a text file and dump it into a excel file
'''
# mypath should be the complete path for the directory containing the input text files
mypath = raw_input("Please enter the directory path for the input files: ")
import os
from os import listdir
from os.path import isfile, join
text_files = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and '.txt' ]


'''
import sys
infile = sys.argv[1]
outfile = sys.argv[2]
'''

def is_number(s):
'''
if the value in the column is number or text
'''
    try:
        float(s)
        return True
    except:
        return False

import xlwt
import xlrd
style = xlwt.XFStyle()
style.num_format_str = '#,###0.00'
row_list=[]
for textfile in text_files:
    with open(textfile,'r+') as f:
        rows=f.readlines()
    for row in rows:
        row_list.append((row.split(' '))
    column_list=zip(*row_list)
    work_book=xlwt.Workbook()
    work_sheet=work_book.add_sheet('Sheet1')
    i=0
    for column in column_list:
        for item in range(len(column)):
            value=column[item].strip()
            if is_number(value):
                work_sheet.write(item,i,float(value),style=style)
            else:
                work_sheet.write(item,i,value)
        i+=1
    work_book.save(textfile.replace('.txt', '.xls'))
                
                        
                    

