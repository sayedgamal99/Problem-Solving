"""
4 8

2 7 5 1

6 1 3 7  >>> k - a[i]

2 4
"""

n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

mapp = dict()
for i in range(n):
    mapp[a[i]]=i

ix,jx = -1,-1

for j in range(n):
    jj = k - a[j]
    if jj in mapp:
        ix,jx = mapp[jj],j
        break

print(ix+1,jx+1)