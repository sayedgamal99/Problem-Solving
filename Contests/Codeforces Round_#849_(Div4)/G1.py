t = int(input().strip())
while(t>0):
    n,c = list(map(int,input().split()))
    liss = list(map(int,input().split()))
    tele = 0
    themap = {}
    for i,val in enumerate(liss):
        if val in themap:
            themap[val].append(i+1)
        else:
            themap[val] = [i+1]
    liss.sort()
    for i in liss:
        if i <= c:

            c -= themap[i][0]
            if(i<=c):
                c-=i
                tele+=1
            themap[i].pop(0)
            


    print(tele)






    t-=1




