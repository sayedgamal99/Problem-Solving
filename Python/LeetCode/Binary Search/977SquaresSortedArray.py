# Basic Solution: 
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums
    

# Binary Search:

# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
        