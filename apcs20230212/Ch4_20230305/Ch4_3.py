results = {"David":0,"Amy":0,"Sean":0}
user = ("David","Amy","Sean")
for i in  range(5):
    vote = input("投給:")
    if vote not in user:
        print("無效")
        continue
    results[vote] = results[vote] + 1
print("選舉結果:")
for name in user:
    print(name,results[name],"票")
    
