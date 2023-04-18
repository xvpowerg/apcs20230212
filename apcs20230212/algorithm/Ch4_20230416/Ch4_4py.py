def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = 9

if is_prime(n):
    print("是質數")
else:
    print("不是質數")
