def count_discinit(strinn):
    res = 0
    liss = []
    for i in strinn:
        if i not in liss:
            res +=1
            liss.append(i)
    return res

# print(count_discinit('str'))

t= int(input().strip())
while(t>0):
    n = int(input().strip())
    stri = input().strip()
    themax = 0
    for i in range(len(stri)-1):
        themax = max(count_discinit(stri[:i+1])+count_discinit(stri[i+1:]),themax)
    print(themax)
    
    t-=1




