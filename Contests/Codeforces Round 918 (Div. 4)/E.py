t = int(input())
i = 0
while(i<t):
    i+=1
    n = int(input())
    glasses = [int(x) for x in input().split()]
    for ii in range(n):
        if ii%2==0: glasses[ii]=glasses[ii]*-1

    sums = [0]
    theset =set(sums)
    theflag = False
    for g in range(n):
        sums.append(sums[-1]+glasses[g])
        if sums[-1] in theset:
            print('YES')
            theflag = True
            break
        theset.add(sums[-1])

    if theflag==False:print('NO')






