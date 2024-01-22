class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        once, n = False, len(nums)
        ind = 0
        while (ind < n-1):
            if nums[ind] <= nums[ind+1]:
                ind += 1
                continue
            if once:
                return False
            if ind == 0 or nums[ind-1] < nums[ind+1]:
                nums[ind] = nums[ind+1]
            else:
                nums[ind+1] = nums[ind]
            once = True
            ind += 1
        return True


# nums = [3,4,2,3]
nums = [1, 5, 1, 6]
print(Solution().checkPossibility(nums))
