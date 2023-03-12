import csv
file = open('data.csv','r')
csvCusor = csv.DictReader(file)

for row in csvCusor:
    print(row['name'],row['score'])
file.close()    
