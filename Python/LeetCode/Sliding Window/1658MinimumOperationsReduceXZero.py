class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums)-x
        l = 0
        current_sum = 0
        max_window = -1
        for r in range(len(nums)):
            current_sum += nums[r]

            while l <= r and current_sum > target:
                current_sum -= nums[l]
                l += 1

            if current_sum == target:
                max_window = max(max_window, r-l+1)

        return len(nums) - max_window if max_window != -1 else max_window


print(Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5))
