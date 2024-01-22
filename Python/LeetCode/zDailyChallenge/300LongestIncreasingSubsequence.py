from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        arr = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>arr[-1]:
                arr.append(nums[i])
            else:
                arr[bisect_left(arr,nums[i])] = nums[i]

        print(arr)
        return len(arr)
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))