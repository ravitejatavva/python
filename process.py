import os
import sys
import time
import re

def get_data(file):
    with open('file.txt' ,'r') as fp:
        data = fp.readlines()
        data_set = set(data)
    return data_set

def get_record_count(file):
#    count = 0
    with open('file.txt' ,'r') as fp:
        data = fp.readlines()
        data_set = set(data)
    return len(data_set)


def main():
    if len(sys.argv)!=3:
        print('command usage: python FileName')
        exit(1)

    else:
#Validation for file1!
            file1 = sys.argv[1]
            # check if the specified file exists or not
            try:
                if os.path.exists(file1):
                        print("file found!")
            except OSError as err:
                print(err.reason)
                exit(1)
                
#validation for file2!                
            file2 = sys.argv[2]
            # check if the specified file exists or not
            try:
                if os.path.exists(file2):
                        print("file found!")
            except OSError as err:
                print(err.reason)
                exit(1)

#get the difference of records from both the files
            set1_data = get_data(file1)
            set2_data = get_data(file2)
            diff_data = set1_data - set2_data
            
            with open('output.txt','w') as fpo:
                for i in range(len(diff_data)):
                    fpo.write(i)
                    
#Deleting the first file once after wirting into the output file!
            try:
                if os.path.isfile(output.txt):
                    os.remove(file1)
                    print("file1 removed!")
            except OSError as err:
                print(err.reason)
                exit(1)

time.sleep(1)

if __name__ == '__main__':
        main()
        
                        
                        

                        
               
        
