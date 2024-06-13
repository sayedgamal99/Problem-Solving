t = int(input())
while t:
    t -= 1
    n, m = [int(x) for x in input().split()]
    maxHashes = 0
    maxrowP = 0
    colCenter = 0
    for i in range(n):
        row = input()
        first = row.find('#')
        hashes = row.count('#')

        if hashes > maxHashes:
            maxHashes = hashes
            maxrowP = i+1
            colCenter = first + ((hashes-1)//2)+1

    print(maxrowP, colCenter)
