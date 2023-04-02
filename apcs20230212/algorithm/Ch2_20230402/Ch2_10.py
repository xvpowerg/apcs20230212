p1 = [1,-3,2]
x = 3
fx = 0
for i in range(len(p1)):
    fx += p1[i] * x ** i
print(f"f({x})={fx}")

p2 = [3,2,2,-3,1,1,0]
y = 3
fy = 0
for k in range(p2[0]):
    fy += p2[2*k + 1] * y ** p2[2*(k + 1)]
print(f"f({y})={fy}")
