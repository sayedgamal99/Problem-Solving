def winners(n, A):
    while True:
        kicked = 0
        for i in A:
            if i <= n:
                kicked += 1
            else:
                break
        if kicked == 0:
            return n
        n = n - kicked


t = int(input())
while t:
    t -= 1
    k, q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    N = [int(x) for x in input().split()]
    for n in N:
        print(winners(n, A), end=' ')
    print()
