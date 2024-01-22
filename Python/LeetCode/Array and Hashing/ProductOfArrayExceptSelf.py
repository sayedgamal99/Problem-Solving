class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod,indd = 1,[]
        prodlist=[]
        numofzeros=0
        for ind,i in enumerate(nums):
            if i == 0:
                numofzeros+=1
                indd.append(ind)
                if numofzeros>1:
                    return [0]*len(nums)
                continue
            prod*=i
            prodlist.append(prod)

        if numofzeros:
            liss = [0]*len(nums)
            liss[indd[0]]=prodlist[-1]
            return liss
        
        for i in range(len(prodlist)):
            prodlist[i]=prodlist[-1]//nums[i]
        return prodlist 
    

A = [-1,1,0,-3,3]
print(Solution().productExceptSelf(A))

