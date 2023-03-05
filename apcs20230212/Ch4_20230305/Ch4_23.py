h = float(input("請輸入身高cm:"))
w = int(input("請輸入體重kg:"))

def bmi(h,w):
    bmi = w /((h /100)**2)
    return bmi
myBmi = bmi(h,w)
print(f"bmi是:{myBmi:.2f}")
