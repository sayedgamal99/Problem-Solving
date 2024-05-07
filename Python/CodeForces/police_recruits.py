numberofcrimes = 0
polices = 0
n = int(input())
events = list(map(int, input().split()))


for i in events:
    if(i==-1):
        if(polices==0):
            numberofcrimes+=1
        else:
            polices-=1
    else:
        polices+=i


print(numberofcrimes)

