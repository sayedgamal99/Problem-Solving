t = int(input())
while t:
    t-=1
    n,k = [int(x) for x in input().split()]
    stringk = ''
    for i in range(k):
        stringk+=chr(ord('a')+i)
    print(stringk*n)
