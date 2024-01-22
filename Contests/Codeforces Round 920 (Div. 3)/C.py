t = int(input())
while t : 
    t-=1

    n,f,a,b = [int(x) for x in input().split()]
    masseges = [int(x) for x in input().split()]

    c_moment = 0
    cost= 0
    ans = 'YES'



    for m in masseges:
        the=(min((m-c_moment)*a,b))
        cost+=the

        c_moment=m
        if cost>=f:
            ans ='NO'
            break



    print('_'*30,ans)




"""
6
1 3 1 5
3
7 21 1 3
4 6 10 13 17 20 26
5 10 1 2
1 2 3 4 5
1 1000000000 1000000000 1000000000
1000000000
3 11 9 6
6 8 10
12 621526648 2585904 3566299
51789 61859 71998 73401 247675 298086 606959 663464 735972 806043 806459 919683

"""