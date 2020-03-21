# first you need to install a py module, run following command
# pip install csv
# importing csv module
import csv, numpy

fields = []
rows = []

# reading csv file
with open(r"C:\Users\asus\Downloads\Edge\GunviolenceSA.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    m=0
    r=None
    for i,row in enumerate(csvreader):
        if int(row[6])+int(row[7])>m:
            m=int(row[6])+int(row[7])
            r = row
        rows.append(row) 

print("Max voilence happens on-",r[0])
