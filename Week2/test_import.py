import utils as u

#Method 1
u.get_file_names("/home/jovyan/python_handin_template")

#Method 2
u.get_all_file_names("/home/jovyan/python_handin_template/Week2")

#Method 3
myList = ["myFile.csv","output.txt","utils.py","week2ex1c.py","Week_2.ipynb"]
u.print_line_one(myList)

#Method 4
list_emails = ["myFile.csv","out@put.txt","utils.py","week2@ex1c.py","Week_2.ipynb"]
u.print_emails(list_emails)

#Method 5
md_list = ["read.md", "readme.md"]
u.write_headlines(md_list)
