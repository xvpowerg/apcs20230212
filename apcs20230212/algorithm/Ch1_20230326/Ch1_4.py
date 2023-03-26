def dec_to_bin(num):
    ns = []
    while True:
        num,reminder = divmod(num,2)
        ns.append(str(reminder))
        if num == 0:
            return "".join(ns[::-1])        
def dec_to_oct(num):
    ns = []
    while True:
        num,reminder = divmod(num,8)
        ns.append(str(reminder))
        if num == 0:
            return "".join(ns[::-1])
        
## A = 10 B = 11 C = 12 D = 13 E = 14 F = 15
def dec_to_hex(num):
    base = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ns = []
    while True:
        num,reminder = divmod(num,16)
        ns.append(base[reminder])
        if num == 0:
            return "".join(ns[::-1])
testNum = int(input("輸入十進位:"))
print("bin:",dec_to_bin(testNum))
print("oct:",dec_to_oct(testNum))
print("hex:",dec_to_hex(testNum))

