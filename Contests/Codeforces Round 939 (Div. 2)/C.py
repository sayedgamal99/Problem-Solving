t = int(input())
while t:
    t -= 1
    n = int(input())

    permutations = [i+1 for i in range(n)]
    s = 0
    k = 1
    for c in permutations:
        s += c*k
        k += 2

    score = s
    operations = (2*n)

    print(score, operations)

    for i in range(n):
        print(1, n-i, *permutations)
        print(2, n-i, *permutations)
