def printMatrix(matrix):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
          print(matrix[i][k],end = ' ')
        print()
matrixA = []

for i in range(2):
    row=[]
    for k in range(3):
        row.append((i+1) ** 2 + (k + 1) ** 2)
    matrixA.append(row)    
printMatrix(matrixA)
