n = int(input())
liss = [int(x) for x in input().split()]

lower,higher,res = liss[0],liss[0],0
for i in range(1,n):
    if liss[i]>higher:
        higher = liss[i]
        res+=1
    elif liss[i]<lower:
        lower = liss[i]
        res+=1
print(res)


