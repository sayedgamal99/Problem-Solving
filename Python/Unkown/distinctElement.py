# n,q = [int(x) for x in input().split()]
# lis = [int(x) for x in input().split()]
# lis.sort()
# ma = lis[-1]
# dislis = [0]*100001
# el = lis[0]
# ndis=0
# for i in lis:
#     if el!=i:
#         ndis +=1
#         dislis[i]=ndis
#         el = i
# while q>0:
#     qq = int(input())
#     print(dislis[qq],dislis[ma]-dislis[qq])
#     q-=1


n,q = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]

lis = list(set(lis))
lis.sort()
dislis = [0]*(lis[-1]+1)
ndis = 0
for i in lis:
    ndis+=1
    # print(i)
    dislis[i]=ndis

prev,key = 0,False
for i,val in enumerate(dislis):
    if val !=0:
        prev = val
        key = True
    elif key :
        dislis[i]=prev


# print(dislis)

while q>0:
    qq = int(input())
    if qq>lis[-1]:
        print(dislis[-1],0)
    else:
        print(dislis[qq-1],dislis[-1]-dislis[qq])
    q-=1
