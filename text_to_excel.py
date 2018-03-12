import os
import sys
import xlwt
import xlrd

#checks whether input given is a number or string/text
def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def get_data(file):
#gets data from a text file
    with open('file.txt','r+') as f:
        data=f.readlines()
    return data

def main():
    if len(sys.argv)!=3:
        print('command usage: python Filename')
        exit(1)
    else:
        infile=sys.argv[1]
        #validation for i/p file
        try:
            if os.path.exists(infile):
                print('file found')
        except OSError as err:
            print(err.reason)
            exit(1)

        outfile=sys.argv[2]
        #validation for output file
        try:
            if os.path.exists(outfile):
                print('file found')
        except OSError as err:
            print(err.reason)
            exit(1)

        #extracting data into a rows data object by using get_data func from an input text file
        rows=get_data(infile)
        row_list=[]
        for row in rows:
            row_list.append(row.split(' '))
        #converting row_wise data into column_wise by using ZIP    
        column_list=list(zip(*row_list))
        work_book=xlwt.Workbook()
        work_sheet=work_book.add_sheet('Sheet1')
        #style for an item in a column if item is a number!!!
        style = xlwt.XFStyle()
        style.num_format_str = '#,###0.00'
        i=0
        for column in column_list:
            for item in column:
                value=column[item].strip()

                if is_number(value):
                    work_sheet.write(item,i,float(value),style=style)
                else:
                    work_sheet.write(item,i,value)
            i+=1
        work_book.save(outfile)
        
            
            
            
