def personInfo(name,age,**other):
    print("name:",name)
    print("age:",age)
    for key in other:        
        print(key,":",other[key])
    print("==========")    
personInfo("Sean",40)
personInfo("David",35,phone="0987655321",company="IBM")
personInfo("Amy",28,email="amy@gmail.com",company="Google")   
    
