greet = "Hi,ed"
print(id(greet),"->",greet)
#greet = greet[:3]+"E"+greet[4:]
#print(greet)
print(id(greet))
greet = greet.replace("e","E")
print(greet)
print(id(greet))
