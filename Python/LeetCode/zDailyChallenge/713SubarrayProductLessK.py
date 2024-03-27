class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        answer, product, l = 0, 1, 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product //= nums[l]
                l += 1
            answer += (r-l+1)
        return answer


print(Solution().numSubarrayProductLessThanK([10, 2, 5, 6], 100))
print(Solution().numSubarrayProductLessThanK([10, 2, 5, 6], 60))
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
