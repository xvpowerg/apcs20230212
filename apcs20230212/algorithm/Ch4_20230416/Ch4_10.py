list_1to9 = [1,2,3,4,5,6,7,8,9]
count=0
for a in list_1to9:
    list_a= list_1to9.copy()
    list_a.remove(a)
    for b in list_a:
     list_b= list_a.copy()
     list_b.remove(b)
     for c in list_b:
        list_c= list_b.copy()
        list_c.remove(c)
        for d in list_c:
         list_d=list_c.copy()
         list_d.remove(d) 
         for e in list_d:
          list_e =list_d.copy()
          list_e.remove(e)
          for f in list_e:
            list_f = list_e.copy()
            list_f.remove(f)
            for g in list_f:
             list_g = list_f.copy()
             list_g.remove(g)
             for h in list_g:
              list_h = list_g.copy()
              list_h.remove(h)
              for i in list_h:
                  count+=1                 
                  if (a/(b*10.+c) + d/(e*10.+f)+g/(h*10.+i)) == 1:
                      print(f'{a}    {d}    {g}')
                      print(f'{b}{c}    {e}{f}    {h}{i}')
                      print()
