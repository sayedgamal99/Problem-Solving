t = int(input())
while t:
    t -= 1
    n = int(input())
    A = [int(x) for x in input().split()]
    Freq = [0]*n

    myscore = 0
    for i in A:
        Freq[i-1] += 1
        if Freq[i-1] == 2:
            myscore += 1
    print(myscore)
