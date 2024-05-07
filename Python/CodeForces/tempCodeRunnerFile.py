f = input().split()
two = input().split()
n,k = int(f[0]),int(f[1])

kk = int(two[k])
# print(kk)
res = k
for i in range(k,len(two)):
    if(int(two[i])==kk):
        res+=1
print(res)


    




