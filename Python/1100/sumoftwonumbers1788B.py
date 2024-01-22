t = int(input())

def summ(n):
    sumj=0
    for _ in range(len(n)):
        sumj+=int(n[_])
    return sumj

def solve():
    n = int(input())
    k1,k2 = n//2,n//2
    if n%2!=0:
        k2+=1
    while(True):
        stk1,stk2=str(k1),str(k2)
        s1,s2=summ(stk1),summ(stk2)
        if abs(s1-s2)<2:
            print(k1,k2)
            break
        elif s1>s2:
            k1-=1
            k2+=1
        elif s2>s1:
            k2-=1
            k1+=1
        
    
while(t):
    solve()
    t-=1