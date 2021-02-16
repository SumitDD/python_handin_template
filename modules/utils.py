import os
import csv

def get_file_names(folderpath, out="output.txt"):

    file_list=os.listdir(folderpath)
    with open(out, 'a') as file_object:
        for file in file_list:
            file_object.write(file + "\n")

get_file_names("/home/jovyan/python_handin_template")

def get_all_file_names(folderpath, out="output.txt"):
    with open(out, 'a') as file_object:
        for root,d_names,f_names in os.walk(folderpath):
            for f_name in f_names:
                    file_object.write(f_name + "\n")

get_all_file_names("/home/jovyan/python_handin_template/Week2")

def print_line_one(file_names):
    
    for file_name in file_names:
        print(file_name.split(".")[0])

myList = ["myFile.csv","output.txt","utils.py","week2ex1c.py","Week_2.ipynb"]
print_line_one(myList)

def print_emails(file_names):
    
     for file_name in file_names:
        if "@" in file_name:
            print(file_name)

list_emails = ["myFile.csv","out@put.txt","utils.py","week2@ex1c.py","Week_2.ipynb"]
print_emails(list_emails)

def write_headlines(md_files, out="output.txt"):
 
    with open(out, 'a') as file:
        for md_file in md_files:
            with open(md_file) as file_object:
                lines = file_object.readlines()
                for line in lines:
                        if line.startswith("#"):
                            file.write(line)

md_list = ["./modules/read.md", "./modules/readme.md"]
write_headlines(md_list)



