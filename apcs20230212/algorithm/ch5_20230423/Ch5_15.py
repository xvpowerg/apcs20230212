cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
while True:
    car = input("車名 Quit離開")
    if car == 'Quit':
        break
    for i in range(len(cars)):
        if cars[i] == car:
            print(f"找到在{i}的位置")
            break
    else:        
        print("找不到")
