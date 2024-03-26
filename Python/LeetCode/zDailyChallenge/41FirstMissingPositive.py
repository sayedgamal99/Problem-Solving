# class Solution:
#     def firstMissingPositive(self, nums: list[int]) -> int:
#         for i in range(len(nums)):
#             if nums[i]<0 : nums[i]=0

#         for i in range(len(nums)):
#             val = abs(nums[i])
#             if 1<= val <= len(nums):
#                 if nums[val-1]>0:
#                     nums[val-1]*=-1
#                 elif nums[val-1]==0:
#                     nums[val-1] = -(len(nums)+1)

#         for i in range(1,len(nums)+1):
#             if nums[i-1]>=0: return i
#         return len(nums)+1


# ------------ another solution --------------
class Solution:
    def firstMissingPositive(self, nums: list[int]):
        nums.sort()
        res = 1
        for n in nums:
            if n < 0:
                continue
            elif n == res:
                res += 1
        return res
