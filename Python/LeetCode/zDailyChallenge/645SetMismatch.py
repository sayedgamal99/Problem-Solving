from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        nn = Counter(nums)
        nn_val = {val:key for key,val in nn.items()}
        duplicated = nn_val[2]
        for i in range(1,len(nums)+1):
            if i not in nn:
                return [i,duplicated]






        
print(Solution().findErrorNums([1,2,2,4]))
print(Solution().findErrorNums([1,1]))