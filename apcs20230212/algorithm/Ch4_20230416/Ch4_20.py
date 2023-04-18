def permute (s):
    out = []
    if len(s) == 1:
        return [s]
    else:
        for i in range(len(s)):        
            for  perm in permute(s[:i]+s[i+1:]):
                  ls = [s[i]]
                  ls.extend(perm)
                  out.append(ls)
    return out
myList = permute([1,2,3,4])
for l in myList:
    print(l)
