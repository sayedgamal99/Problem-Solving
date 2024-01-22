# 4
# 3
# 1 0 1
# 3
# 0 1 1
# 4
# 1 0 0 1
# 1
# 0


# 3
# 7
# -1
# 1


t= int(input())
while(t>0):
    t-=1
    n = int(input())
    days = [int(x) for x in input().split()]
    high,die = 2 if days[0] else 1,0 if days[0] else 1
    for i in range(1,n):
        if days[i] and days[i-1]:
            high +=5
            die=0
        elif days[i] :
            high +=1
            die=0
        else:
            die+=1
        if die>1:
            break


    print(-1) if die>1  else print(high)
