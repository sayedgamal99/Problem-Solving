line = list(map(int,input().split()))
n = line[0]
k = line [1]
while k>0:
    if n % 10 == 0:
        n = n/10
    else:
        n -=1
    k-=1
print(int(n))