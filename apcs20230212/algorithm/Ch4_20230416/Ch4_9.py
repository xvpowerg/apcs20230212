def square_root2(x,pre=2):
    r = 0
    step = 1
    while step >= 10 **-(pre):
        while (r*r < x):
            r += step
            if  r * r == x:
                return r
        r -= step
        step /= 10
    
    return r

print(square_root2(11))
print(f"{square_root2(2):.2f}")
