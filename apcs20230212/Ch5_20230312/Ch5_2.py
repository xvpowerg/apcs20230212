str_result=input('字母接龍\n請輸入字串:')
eCount=0
while(eCount<5):    
    print('目前字串:%s' %str_result)
    str_in = input('請輸入-%s-開始的字串:' %str_result[-1].upper())
    if(str_in[0].lower()==str_result[-1].lower()):
        str_result+="-"+str_in
    else:
        eCount += 1
        print('輸入錯誤%d次' %eCount)

print('錯誤超過五次,遊戲結束!')
