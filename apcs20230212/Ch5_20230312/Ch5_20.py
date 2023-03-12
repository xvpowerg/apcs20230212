filename = "abc.txt"
fin = open(filename)
line = fin.readline()

while line:
    print(line,end='')
    line = fin.readline() 
