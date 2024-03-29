class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        overall_subarrays = (n*(n+1))//2

        max_element = max(nums)
        l = 0
        mFreq = 0
        answer = 0
        for r in range(len(nums)):
            if nums[r] == max_element:
                mFreq += 1
            while l <= r and mFreq == k:
                if nums[l] == max_element:
                    mFreq -= 1
                l += 1

            if mFreq < k:
                answer += (r-l+1)

        return overall_subarrays - answer


print(Solution().countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print(Solution().countSubarrays([61, 23, 38, 23, 56, 40, 82, 56, 82,
      82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], 2))
