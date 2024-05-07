f = input().split()
two = input().split()
n, k = int(f[0]), int(f[1])

kk = int(two[k-1])
# print(kk)
res = 0
for i in range(n):
    if int(two[i]) >= kk and int(two[i]) != 0:
        res += 1
print(res)
