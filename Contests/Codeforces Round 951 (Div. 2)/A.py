# A. Guess the Maximum (ACC)

def winner(n, A):
    maxs = set()
    for i in range(1, n):
        maxs.add(max(A[i], A[i-1]))
    ans = min(maxs)
    return ans-1


t = int(input())
while t:
    t -= 1
    n = int(input())
    A = [int(x) for x in input().split()]
    print(winner(n, A))
    print()
