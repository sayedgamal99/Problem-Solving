t = int(input())
for _ in range(t):
    x, y, z, k = map(int, input().split())
    ans = 0
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            if k % (a * b) != 0:
                continue
            c = k // (a * b)
            if c > z:
                continue
            ways = (x - a + 1) * (y - b + 1) * (z - c + 1)
            ans = max(ans, ways)
    print(ans)
