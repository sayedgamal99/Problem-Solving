t = int(input())

while (t):
    t -= 1
    n, m = [int(x) for x in input().split()]
    n = [int(x) for x in input().split()]
    m = [int(x) for x in input().split()]

    n.sort()
    m.sort(reverse=True)

    l,r = 0,len(n)-1
    rr = len(m)-1

    maxxsum = 0
    while (l<=r):

        rsum, lsum = abs(n[r]-m[rr]), abs(n[l]-m[l])
        if lsum>rsum:
            maxxsum+=lsum
            l+=1
        else:
            maxxsum+=rsum
            r-=1
            rr-=1

        # if l+1 == r:
        #     maxxsum += max(abs(n[l+1]-m[l+1]),abs(n[r-1]-m[rr-1]))
        #     break



    print('kkkkkkkkkk',maxxsum)

    

"""
3
3 5
6 5 2
1 7 9 7 2
5 5
9 10 6 3 7
5 9 2 3 9
1 6
3
2 7 10 1 1 5
5 6
1 2 3 4 5
40 30 20 10 2 1
"""