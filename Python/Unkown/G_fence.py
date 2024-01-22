def minimum_con_array(arr,n,k):
    i1,i2 =-1,0
    result = (0,99999999) # store index, minimum value
    prfx,summ=[],0
    while(i2<n):
        summ+=arr[i2]
        prfx.append(summ)
        if i2+1>=k:
            mini = prfx[i2]-(prfx[i1] if i1!=-1 else 0)
            if mini <= result[1]:
                result = (i1+2,mini)
            i1+=1
        i2+=1
    return result


n,k = [int(x) for x in input().split()]
hights = [int(x) for x in input().split()] 
print(minimum_con_array(hights,n,k))

