H =int(input("樹高")) 
D =int(input("白天上升"))
N =int(input("晚上下降"))

height = D
days=1
while height < H:
    height -= N
    height += D
    days += 1
print("days:",days)   
