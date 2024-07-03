class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 4:
            # If there are 4 or fewer elements, we can remove all elements or none,
            # making the minimum difference 0.
            return 0

        moves = 3
        nums.sort()  # Sort the array

        minimum = float('inf')

        # Compare the differences for the four possible ways to remove 3 elements:
        for i in range(moves + 1):
            minimum = min(minimum, nums[n - moves - 1 + i] - nums[i])

        return minimum


print(Solution().minDifference(nums=[1, 5, 0, 10, 14]))  # 1
print(Solution().minDifference(nums=[0, 5, 10, 20, 21, 30, 40]))  # 16
