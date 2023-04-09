def flip(matrixA):
    matrixB = []
    r = len(matrixA)
    for i in range(r-1, -1, -1): #A的index:2資料 放到 Ｂ index:0的資料
        print("i:",i)
        matrixB.append(matrixA[i])
    return matrixB

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

m1 = [[1,4],[2,5],[3,6]]
m2 = flip(m1)
printMatrix(m1)
print('翻轉後...')
printMatrix(m2)

a1 = [5,6,7,8]
print(a1[-1])
