def canPlaceFlowers(flowerbed, n):
    key = 0 if flowerbed[0] else 1
    for i in flowerbed:
        if i == 1:
            n -= int((key-1)/2)
            key = 0
        else:
            key += 1
    n -= (key//2)
    return n <= 0
