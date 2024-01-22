class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums)

        while left < right:
            mid = left+(right-left) // 2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left
