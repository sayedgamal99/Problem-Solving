from collections import Counter
t = int(input())
while t:
    t -= 1
    n, k,m = [int(x) for x in input().split()]
    ss = input()
    stringk = ''
    for i in range(k):
        stringk += chr(ord('a')+i)

    themap = Counter(stringk*n)
    tocheck = Counter(ss)

    if set(themap.values()) !=set(tocheck.values()):
        if set(themap.keys()) !=set(tocheck.keys()):
            pickLetter = set(themap.keys()).difference(set(tocheck.keys()))

            print('NO')
            print(str(pickLetter.pop())*n)
        else:
            print('NO')
            vv = {val:key for key,val in tocheck.items()}
            print(vv[min(vv)]*n)

    elif themap==tocheck:
        if len(Counter(ss[:n]))<k:
            print('NO')
            print(stringk)
        else:
            print('YES')

"""
tests:

5
2 2 4
abba
2 2 3
abb
3 3 10
aabbccabab
3 3 10
aabbababab
3 3 12
cccbbbaaa


"""
