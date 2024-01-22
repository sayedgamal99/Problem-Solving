"""
5
2
aa
7
abcabcd
5
aaaaa
10
paiumoment
4
aazz

2
7
2
10
3

"""
t = int(input())
while(t):
    t-=1
    n = int(input())
    saso=input()
    resl,rresl,num,rnum = [],[],0,0
    liss,rliss = [],[]
    for letter,rletter in zip(saso,reversed(saso)):
        if letter not in liss:
            num+=1
            liss.append(letter)
        resl.append(num)

        if rletter not in rliss:
            rnum+=1
            rliss.append(rletter)
        rresl.append(rnum)
    rresl.reverse()


    maxx,j = 0,0
    for i in reversed(range(1,len(resl))):
        maxx = max(maxx,(resl[i-1]+rresl[i]))
    print(maxx)


