sq1 = [x for x in range(1,10) ]
print(sq1)
sq2 = {x for x in range(1,10) if x %2 != 0}
print(sq2)
sq3 = {x:x*x for x in range(1,10)}
print(sq3)
sq4 = [x + 10 for x in range(1,10) if x % 2 == 0]
print(sq4)
ces = [v for v in range(0,101,10)]
print(ces)
fah = [9/5 * x + 32 for x in ces]
print(fah)
