"""

3
6
2 2 1 2 1 2
3
1 2 1
4
1 1 1 1


2
-1
1

"""

t = int(input())
while(t):
    t-=1
    n = int(input())
    numbers = [int(x) for x in input().split()]
    resulting,sum = [],1
    for i in numbers:
        sum*=i
        resulting.append(sum)
    # print(resulting)
    res = -1
    for i in range(n):
        # print(resulting[i], resulting[-1]//resulting[i])
        if resulting[i] == resulting[-1]//resulting[i]:
            res = i+1
            break
    print(res)