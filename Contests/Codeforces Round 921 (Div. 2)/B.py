import math
t = int(input())
while t : 
    t-=1
    x,n = [int(x) for x in input().split()]
    if x%n!=0:
        k = x%n
        kk =  n- x%n

        k1 = (x//n)+k
        k2 = (x//n)-k
        if k1==0 or k2==0:
            print(math.gcd(min(k1,k2),min(k,kk)))
        else:
            print(math.gcd((x//n)+k,((x//n)-k)))
    else:
        print(x//n)