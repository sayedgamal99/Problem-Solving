from collections import Counter as co
t = int(input())
i = 0
while (i<t):
    flag =True
    for j in range(3):
        kk = input()
        if flag == False:
            continue
        theset = set(kk)
        for l in 'ABC':
            if l not in theset:
                answer = l;flag=False;break
    print(l)
    i+=1

