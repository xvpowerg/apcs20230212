coinType=(50,10,5,1)
def exchange(amt):
    dp = [amt + 1] * (amt + 1)                  # 構建dp動態陣列
    dp[0] = 0                                   # 初始化
    
    for i in range(1, amt + 1):
        temp = [dp[i]]                          # 每一個金額，所有能湊成的方案的硬幣數，最後取最小值
        for coin in coinType:
            if i >= coin:
                temp.append(dp[i-coin]+1)       # 當金額大於某一個硬幣時才考慮，否則一定無法用大額硬幣湊成小額
        dp[i] = min(temp)
    #print(dp)
    return -1 if dp[-1] == amt + 1 else dp[-1]

count = 0
amount = int(input('輸入兌換金額:'))
answer=exchange(amount)
print('最少需換成%d個硬幣'%answer)
