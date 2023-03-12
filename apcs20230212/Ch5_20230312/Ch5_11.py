scores = {'Ch':100,'En':80,'Ma':95}
print(scores)
print(scores.keys())
print(scores.values())
print(scores.items())

add_dic = {"So":90}
scores.update(add_dic)
#scores["SO"] = 90
print(scores)
add_dic = {"Ma":'N/A'}
scores.update(add_dic)
print(scores)

ch1 = scores.get("Ch")
print(ch1)
en1 = scores.get("EN","N/A")
print(en1)
so1 = scores.pop("So",'N/A')
print(so1)
print(scores)
