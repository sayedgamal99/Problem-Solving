num1 = [int(x) for x in input().split()]
num2 =[int(x) for x in input().split()]
the = dict()
s2=len(num2)
for index,el in enumerate(num2):
    for i in range(index,s2):
        if num2[i]>el:
            the[el]=num2[i]
            break
        if el not in the:
            the[el]=-1
result = [the[x] for x in num1]
print(result)




