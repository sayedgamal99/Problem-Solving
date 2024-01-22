n = int(input())
i=0
while(i<n):
    ss = [int(x)for x in input().split()]
    mapp = {}
    for j in range(3):
        mapp[ss[j]] = mapp.get(ss[j],0)+1
    for k,v in mapp.items():
        if v==1: print(k)
    i+=1