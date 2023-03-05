def c2f(c):
    f = 9 / 5 * c + 32
    return f

while(True):
    inStr = input("輸入攝氏溫度q離開")
    if  inStr == 'q':
        print("結束")
        break
    tc = float(inStr)
    f = c2f(tc)
    print(f"華氏溫度:{f:.2f}")
