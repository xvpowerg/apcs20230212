poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉'''
"""
try:
    file = open('output2.txt','w')
    file.write(poem)
    file.flush()
    file.close()
    print("完成!")
except Exception as e:
    print(e)
"""

try:
    with open('output2.txt','w') as f:
        f.write(poem)    
        print("完成!")
except Exception as e:
    print(e)
