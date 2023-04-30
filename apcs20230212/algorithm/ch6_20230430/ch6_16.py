coinType = (50,10,5,1)
def exchange(amt):
    global count
    result={}
    for coin in coinType:
        num = amt // coin
        result[coin] = num
        count+=num
        amt %= coin
    return result  
count =0 
amount = int(input("輸入金額"))
ans = exchange(amount)
for coin in coinType:
    print(f"{coin}元硬幣{ans[coin]}個")
print(f"共{count}個硬幣")   
