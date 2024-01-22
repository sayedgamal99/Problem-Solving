def pivot(nums):
    suml,sumr=0,0
    lenn = len(nums)
    liss = [0]*(lenn+2)
    for i,val in enumerate(nums):
        suml+=val
        liss[i+1]=suml
    liss[0],liss[-1]=0,0
    print(liss)
    for i in range(lenn):
        print(f"{liss[lenn]} - {liss[i+1]} == {liss[i]}")
        try:
            if (liss[lenn] - liss[i+1]) == liss[i]:
                return i
        except:
            continue
        
    return(-1)





A = [int(x) for x in input().split()]
print(pivot(A))



"""
1 7 3 6 5 6
[1 8 11 17 22 28]

"""