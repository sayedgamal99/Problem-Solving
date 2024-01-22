t = int(input())


def solve():
    n = [int(x) for x in input().split()]
    n.sort()
    print(n[1])


while (t):
    solve()
    t -= 1
