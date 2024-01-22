"""
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        mapp = {0:-1}
        for number in nums:
            if number>=0:
                pos = True if number+1 in mapp else False
                pre = True if number-1 in mapp else False
                mapp[number]=-1
                if pos:mapp[number]=number+1
                if pre:mapp[number-1]=number
        result = float('inf')
        for key,val in mapp.items():
            if val==-1:
                result = min(result,key)
        del mapp
        return result+1

"""


"""
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        result = 1
        theset = set(nums)
        for _ in range(len(nums)):
            if result in theset:
                result+=1
        return result
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0 : nums[i]=0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1<= val <= len(nums):
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1]==0:
                    nums[val-1] = -(len(nums)+1)
        
        for i in range(1,len(nums)+1):
            if nums[i-1]>=0: return i
        return len(nums)+1

# liss = [1,2,0]
liss=[1,5,6,7,8]
print(Solution().firstMissingPositive(liss))