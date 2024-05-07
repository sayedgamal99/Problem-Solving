t = int(input())
while (t):
    t-=1
    n,m = [int(x) for x in input().split()]
    s1= input()
    s2=input()
    s = s1+s2[::-1]
    res = 0
    for i in range(1,len(s1)+len(s2)):
        if s[i]==s[i-1]:
            res+=1
    if res>1:
        print('NO')
    else:
        print('YES')



