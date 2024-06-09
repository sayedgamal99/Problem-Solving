n, l, r = [int(x) for x in input().split()]
l -= 1
r -= 1

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve():
    s1 = 0
    s2 = 0
    for i in range(l, r+1):
        s1 += A[i]
        s2 += B[i]

    if s1 == s2:
        for i in range(l):
            if A[i] != B[i]:
                return "LIE"
        for i in range(r+1, n):
            if A[i] != B[i]:
                return "LIE"
        return "TRUTH"
    else:
        return 'LIE'


print(solve())
