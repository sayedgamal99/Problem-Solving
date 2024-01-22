a,b,x = [int(x)for x in input().split()]
c = ((b//x))
c = (c*x)*(c+1)//(2)
s = (a-1)//x
s = (s*x)*(s+1)//2
ans=c-s
summ = 0
if a>b : 
    temp = b
    b = a
    a = temp
for i in range(a,b+1):
    if i%x==0:
        summ+=i

print(abs(ans))
print(summ)