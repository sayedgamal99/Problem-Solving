



def solve():
    n = int(input())
    b = [int(x) for x in input().split()]
    a = []
    a.append(b[0])
    for i in range(1,n-1):
        a.append(min(b[i],b[i-1]))
    a.append(b[-1])
    print(*a)
t = int(input())
for _ in range(t):
    solve()
