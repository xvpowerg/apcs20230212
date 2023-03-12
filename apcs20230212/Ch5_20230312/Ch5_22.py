import csv
file = open('data2.csv','r')
csvCusor = csv.reader(file)

for row in csvCusor:
    print(row[0],row[2])

file.close()    
