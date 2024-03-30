class Solution:
    def subarrayswithAtmostKdistinct(self, nums, k):
        themap = {}
        l = 0
        answer = 0
        for r in range(len(nums)):
            themap[nums[r]] = themap.get(nums[r], 0)+1
            length = len(themap.keys())
            while length > k:
                themap[nums[l]] -= 1
                if themap[nums[l]] == 0:
                    del themap[nums[l]]
                    length -= 1
                l += 1
            answer += (r-l+1)
        return answer

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.subarrayswithAtmostKdistinct(nums, k)-self.subarrayswithAtmostKdistinct(nums, k-1)


print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
print(Solution().subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
