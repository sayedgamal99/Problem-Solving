import itertools
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prfx = list(itertools.accumulate(nums))
        # prfx = [sum(nums[:i+1]) for i in range(len(nums))]
        hash = {0:-1}
        for ind,j in enumerate(prfx):
            res = j%k
            if res in hash:
                istwo = ind-hash[res]
                print(istwo,hash)
                print(prfx)
                return True 
            else:
                hash[res] = ind
        
                
        return False
    


arr = [24,50,6,4,1]
print(Solution().checkSubarraySum(arr,8))