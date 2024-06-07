# xor sequence (ACC)
t = int(input())
while t:
    t -= 1
    x, y = [int(x) for x in input().split()]

    xor = x ^ y
    print((xor & -xor))
