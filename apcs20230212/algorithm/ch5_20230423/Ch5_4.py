import random

def guessCheck(gus, low, high):
    #print("guessCheck(%d, %d, %d, %d)"%(ans, gus, low, high))
    global answer
    if answer==gus:
        print('猜對了!')
    else:
        if(answer>gus):
            low=gus+1
        else:
            high=gus-1
        guess = int(input('猜一個%d~%d的整數:'%(low,high)))
        return guessCheck(guess, low, high)


start, end = 1, 100
answer = random.randint(start, end)
#print(answer)
guess = int(input('猜一個%d~%d的整數:'%(start,end)))
guessCheck(guess, start, end)
