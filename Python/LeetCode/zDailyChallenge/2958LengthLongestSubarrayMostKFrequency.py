class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        themap = {}
        l = 0
        max_length = 0
        for r in range(len(nums)):
            themap[nums[r]] = themap.get(nums[r], 0)+1
            if themap[nums[r]] > k:
                while l <= r:
                    C = nums[l]
                    themap[C] -= 1
                    l += 1
                    if C == nums[r]:
                        break

            max_length = max(max_length, r-l+1)

        return max_length


print(Solution().maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
