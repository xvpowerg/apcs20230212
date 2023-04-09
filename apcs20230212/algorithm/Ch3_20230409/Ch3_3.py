def rotate(matrixA):
    matrixB = []
    r = len(matrixA)
    c = len(matrixA[0])
    for i in range(c):
        row = []
        for j in range(r-1, -1, -1):
            row.append(matrixA[j][i]) #colum不變 row由最後一筆開始往上
        matrixB.append(row)
    return matrixB

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


m1 = [[3,6],[2,5],[1,4]]
m2 = rotate(m1)
printMatrix(m1)

print('旋轉後...')
printMatrix(m2)
print('===========')

