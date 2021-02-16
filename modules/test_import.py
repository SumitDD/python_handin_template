import modules.utils as u

#Method 1
u.get_file_names("./modules/")

#Method 2
u.get_all_file_names("./modules/")

#Method 3
myList = ["myFile.csv","output.txt","utils.py","week2ex1c.py","Week_2.ipynb"]
u.print_line_one(myList)

#Method 4
list_emails = ["myFile.csv","out@put.txt","utils.py","week2@ex1c.py","Week_2.ipynb"]
u.print_emails(list_emails)

#Method 5
md_list = ["./modules/read.md", "./modules/readme.md"]
u.write_headlines(md_list)
