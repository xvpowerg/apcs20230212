for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if k == j or k == i:
                continue
            for l in range(1,5):
                   if l == k or l == j or l==i:
                       continue
                   print(f"{i} {j} {k} {l}")
