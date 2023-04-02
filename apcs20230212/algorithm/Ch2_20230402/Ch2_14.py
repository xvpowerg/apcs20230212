def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def matrixTranspose(A):
    m = len(A)#3
    n = len(A[0])#4
    #B = [[None]*m for row in range(n)]
    B = []
    for i in range(n):
        tp=[]
        for j in range(m):
            #B[i][j] = A[j][i]
            tp.append(A[j][i])
        B.append(tp)
    return B


matrixA = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrixB = matrixTranspose(matrixA)

print("MatrixA:")
printMatrix(matrixA)
print("MatrixB:")
printMatrix(matrixB)
