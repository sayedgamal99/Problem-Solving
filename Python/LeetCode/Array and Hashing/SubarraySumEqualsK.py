class Solution:
    def subarraySum(self,nums,k):
        res = 0
        hashh,sum = {0:1},0
        for i in nums:
            sum+=i
            diff = sum-k
            res += hashh.get(diff,0)
            hashh[sum] = hashh.get(sum,0)+1
        return res







# A = [-2,5,2,3,1,1,-4,6]
A= [1,-1,1,1,1,1]
# A = [1,1,1]
# A = [1,2,3]
print(Solution().subarraySum(A,3))



"""
Time limit exceeded in this brute force solution.

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        n=len(nums)
        for i in range(n):
            sum = 0
            for ii in range(i,n):
                sum+=nums[ii]
                if sum==k:
                    result+=1
        return result

"""