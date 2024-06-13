t = int(input())
while t:
    t -= 1
    a, b = input().split()
    newA = b[0]+a[1:]
    newB = a[0] + b[1:]
    print(newA, newB)
