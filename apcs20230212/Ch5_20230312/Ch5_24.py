import random
ans = random.randint(1,5)
guess = int(input("1~5:"))
if (guess == ans):
    print("答對了!")
else:
    print("答錯了!")    
