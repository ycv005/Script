# first you need to install a py module, run following command
# pip install csv
# importing csv module 
import csv, numpy

fields = []
rows = []

def to_dic(l):
    l= l.strip('][').split(", ") 
    l=[i.replace("'", "") for i in l]
    l=list(set(l))
    return l

# reading csv file 
with open(r"C:\Users\asus\Downloads\Edge\dataset.csv", 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row 
    fields = next(csvreader)
  
    # extracting each data row one by one 
    for row in csvreader:
        row[1] = to_dic(row[1])
        rows.append(row) 

# print(fields)
# print(rows[:5])

with open(r"C:\Users\asus\Downloads\Edge\new_dataset.csv", 'w',newline="") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)
