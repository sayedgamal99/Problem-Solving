t = int(input())
i = 0
while (i<t):
    i+=1
    n = int(input())
    nums = [int(x)for x in input().split()]
    summ = sum(nums)
    answer = 'YES' if (summ**.5)%1==0 else 'NO'
    print(answer)
