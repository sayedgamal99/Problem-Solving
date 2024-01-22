nums = [int(x)for x in input().split()]
winner = dict()
key = 0
for i in nums:
    if i in winner:
        winner[i]+=1
        if winner[i]>key:
            key = i
    else:
        winner[i]=1


print(key)

