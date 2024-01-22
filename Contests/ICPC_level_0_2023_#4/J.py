"""
4
6
3 5 1 4 6 6
3
1 2 3
4
1 3 3 4
6
1 6 3 4 5 6

1
3
3
10


"""

t = int(input())
while(t):
    t-=1
    n = int(input())
    numbers = [int(x) for x in input().split()]
    res = 0
    for x in range(n):
        for y in range(x+1,n):
            if numbers[y]-numbers[x] == y-x:
                res+=1
    print(res)