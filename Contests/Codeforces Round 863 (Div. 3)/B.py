def layer(x,y,n):
    return min(x,y,n+1-x,n+1-y)

def solve():
    n,x1,y1,x2,y2 = [int(x) for x in input().split()]
    print(abs(layer(x1,y1,n)-layer(x2,y2,n)))

t = int(input())
for _ in range(t):
    solve()