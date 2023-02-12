coin1 = 20
coin5 = 10
coin10 = 3
coin50 = 2
coin_total = coin50 * 50  + coin10 * 10 + coin5 * 5 + coin1
print("金幣總額:",coin_total)
b100 = 3
b200 = 2
b500 = 1
b1000 = 2
b_total = (b100 + b200 * 2 + b500 * 5 + b1000 * 10)  * 100
print("紙鈔金額:",b_total)

print("總額:",b_total + coin_total)
