# 5 3
# 2 1 3 5 2
# 1 1
# 3 3
# 5 5


# 2
# 3
# 2


n,q = [int(x) for x in input().split()]
games = [int(x) for x in input().split()]
results = [0]
sum =0
for i in games:
    sum+=i
    results.append(sum)
while (q):
    l,r = [int(x) for x in input().split()]
    print(results[r]-results[l-1])
    q-=1
    
