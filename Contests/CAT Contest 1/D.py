t = int(input())


def solve():
    n = int(input())
    strr = input()
    origi = n
    for i,j in zip(strr,reversed(strr)):
        if i !=j:
            origi-=2
        else:
            print(origi)
            return
    print(0)





while(t):
    solve()
    t-=1

