# first you need to install a py module, run following command
# pip install csv
# importing csv module 
import csv, numpy
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
def addMonths(l):
    r=[]
    for i in range(1, 13):
       r.append(str(l)+"-"+str(i))
    return r

# reading csv file 
with open(r"C:\Users\asus\Downloads\Edge\wind_west_pacific.csv", 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row 
    fields = next(csvreader)
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

year = []
data = []
# res = [[]]
for row in rows: 
    # parsing each column of a row 
    year += addMonths(row[0])
    data += row[1:]

# print(year)
# print(data)
res = list(zip(year, data))
# print(res)

with open(r"C:\Users\asus\Downloads\Edge\new-wind_west_pacific.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(res)
