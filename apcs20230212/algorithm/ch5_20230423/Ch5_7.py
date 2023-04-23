#p1 來源
#p2 中繼
#p3 目標
def hanoi(n, p1, p2, p3):
    if n==1: # 遞迴出口
        print(f'{n}套環從 {p1} 移到 {p3}' )
    else:
        hanoi(n-1, p1, p3, p2)#來源P1 P3改為中繼 P2改為目標  來源不變
        print(f'{n}套環從 {p1} 移到 {p3}' )
        #print('%d套環從 %s 移到 %s' %(n, p1, p3))#n-1完成後把最大的放到目標柱
        hanoi(n-1, p2, p1, p3)#中繼(P2)來源改為 來源改為P1中繼為 目標是P3

i=int(input('請輸入套環數量：'))
hanoi(i,'A', 'B', 'C')
