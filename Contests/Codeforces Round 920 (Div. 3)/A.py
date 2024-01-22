t = int(input())
while (t):
    t-=1
    ys,xs= [],[]
    for i in range(4):
        x,y = [int(x) for x in input().split()]
        ys.append(y)
        xs.append(x)

    area = (max(ys)-min(ys))*(max(xs)-min(xs))
    print(area)


