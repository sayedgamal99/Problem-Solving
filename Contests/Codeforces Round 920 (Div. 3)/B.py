t = int(input())
while t:
    t -= 1
    n = int(input())

    inn = input()
    ott = input()

    result = bin(int(inn,2) ^ int(ott,2))[2:]

    inn_modified = ''
    for jj in range(len(inn)):
        if inn[jj]!=ott[jj]:
            inn_modified+=inn[jj]

        
    number_of_changes = min(inn_modified.count('1'), inn_modified.count('0'))

    xor = result.count('1')

    print(xor-number_of_changes)




""""
6
5
10010
00001
1
1
1
3
000
111
4
0101
1010
3
100
101
8
10011001
11111110

"""