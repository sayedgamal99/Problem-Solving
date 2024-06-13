t = int(input())
while t:
    t -= 1
    n = int(input())
    answer = 0
    winner = 0
    for j in range(n, 1, -1):

        for i in range(2, j+1):
            if j % i != 0:
                continue
            numbers = n//i
            A = i * (numbers*(numbers+1)//2)
            if A > answer:
                answer = A
                winner = i
    print(winner)
