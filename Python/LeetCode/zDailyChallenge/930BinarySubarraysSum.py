class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            l, answer = 0, 0
            currentSum = 0

            for r in range(len(nums)):
                currentSum += nums[r]
                while currentSum > x:
                    currentSum -= nums[l]
                    l += 1
                answer += (r-l+1)
            return answer

        return helper(goal)-helper(goal-1)


print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
