t = int(input())
while t:
    t -= 1
    n = int(input())
    A = [int(x) for x in input().split()]
    preS = 0
    answer = 0
    mx = 0
    for i in range(n):
        preS += A[i]
        mx = max(A[i], mx)
        if preS-mx == mx:
            answer += 1
    print(answer)
