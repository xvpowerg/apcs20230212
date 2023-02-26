carList = ['Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda']
carSet  = {'Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda'}
print(carList)
print(carList[2-1])
print(len(carSet),carSet)

targetCar = {'Audi','Benz','BMW'}
carDict = {'Audi':0,'Benz':0,'BMW':0}
for car in carList:
    if (car in targetCar):
        #print(car)
        carDict[car] += 1
print(carDict)        
