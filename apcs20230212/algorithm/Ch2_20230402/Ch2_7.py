num = int(input("輸入數量"))
arr = [0] * num
for i in range(num):
    arr[i] = int(input(f'{i+1}.輸入陣列內容:'))
for k in range(num-1):
    if arr[k] * arr[k+1]>=0 :
        print("不是正負交錯")
        break
else:
    print("是正負交錯")
print(arr)    
