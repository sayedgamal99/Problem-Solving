t = int(input())

def solve():
    n = int(input())
    liss = [int(x) for x in input().split()]
    if n ==1 :
        print("YES")
        return

    liss.sort()
    i=1
    while(i<len(liss)):
        if abs(liss[i]-liss[i-1])<2:
            liss.pop(i-1)
            i-=1
        i+=1
    print("YES" if len(liss)==1 else "NO")

        

while(t):
    solve()
    t-=1
