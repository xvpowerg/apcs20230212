answer = 5
for i in range(5):
    guess = int(input("猜一個數字"))
    if guess == answer:
        print('猜對了')
        break
else:
    print("答案是:",answer)

    
    
