arr=[[0]*6 for row in range(6)]             #宣告矩陣arr

data=[[1,2],[2,1],[1,5],[5,1],              #圖形各邊的起點值及終點值
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3]]
for i in range(10):                         #讀取圖形資料
    tmpi=data[i][0]                 #tmpi為起始頂點
    tmpj=data[i][1]                 #tmpj為終止頂點
    arr[tmpi][tmpj]=1               #有邊的點填入1

print('無向圖形矩陣：')
for i in range(1,6):
    for j in range(1,6):
        print('[%d] ' %arr[i][j],end='')    #列印矩陣內容
    print()
