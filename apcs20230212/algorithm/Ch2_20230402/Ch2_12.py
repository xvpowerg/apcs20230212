def printMatrix(matrix):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
          print(matrix[i][k],end = ' ')
        print()
matrixA = [[0]*2  for x in range(3)]

for i in range(len(matrixA)):
    for k in range(len(matrixA[i])):
        matrixA[i][k] = 2 * (i + 1) + (k + 1)

printMatrix(matrixA)
