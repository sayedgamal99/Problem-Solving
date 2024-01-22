t= int(input().strip())
while(t>0):
    key  = 0

    point = [0,0]
    n = int(input().strip())
    strr = input().strip()
    for i in strr:
        if i == 'U':
            point[1]+=1
        elif i == 'D':
            point[1]-=1
        elif i == 'L':
            point[0]-=1
        elif i == 'R':
            point[0]+=1
        if (point[0] == 1 and point[1] ==1):
            print('Yes')
            key = 1
            break
    if key == 0:
        print('No')
    t-=1


