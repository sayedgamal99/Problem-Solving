t= int(input().strip())
while(t>0):
    n = int(input().strip())
    liss = list(map(int,input().split()))
    liss.sort()
    summ = 0
    neg = 0
    for i in liss:
        if i < 0:
            neg+=1
    if neg%2 == 0:
        for ii,ll in enumerate(liss):
            if ll<0:
                liss[ii] = -1*liss[ii]
    else:
        for ii,ll in enumerate(liss):
            if ll<0:
                liss[ii] = -1*liss[ii]
        liss.sort()
        liss[0] = -1*liss[0]
    for iii in liss:
        summ+=iii
            
            

    print(summ)
    t-=1




