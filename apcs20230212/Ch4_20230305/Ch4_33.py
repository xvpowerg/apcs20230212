str1 = "The is his dogs"
search1 = "is"
print( str1.find(search1))
print( str1.rfind(search1))
print( str1.find(search1,5))
print( str1.rfind(search1,10))#回傳-1

print(str1.index(search1,5,12))
print(str1.rindex(search1,5,12))
print(str1.rindex(search1,10))#找不到拋出錯誤



