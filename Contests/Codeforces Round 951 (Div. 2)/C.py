# C- Earning bets
# brute force solution (TLE)
def bet(n, A):
    m = 10000
    ANS = [1]*n
    cSum = n
    while (m):
        m -= 1
        modify = True
        for i in range(n):
            if ANS[i]*A[i] <= cSum:
                cSum += 1
                ANS[i] += 1
                modify = False
        if modify:
            return ANS
    return -1


t = int(input())
while t:
    t -= 1
    n = int(input())

    A = [int(x) for x in input().split()]
    ans = bet(n, A)
    if ans == -1:
        print(-1)
    else:
        print(*ans)
