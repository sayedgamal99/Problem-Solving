q = int(input())
while(q):
    q-=1
    n,d = [int(x) for x in input().split()]
    number = input()
    key = 1
    for ind,i in enumerate(number):
        if d>int(i):
            number = number[:ind]+str(d)+number[ind:]
            key = 0
            break
    if key==1:
        number=number+str(d)
    print(number)
