# try brute force first: ... it works but got tle
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        result = 0
        for i in range(n-1, 0, -1):
            kk = k
            freq = 1
            for j in range(i-1, -1, -1):
                if nums[j]+kk >= nums[i]:
                    kk -= (nums[i]-nums[j])
                    freq += 1
                elif nums[j] == nums[i]:
                    freq += 1
                else:
                    break
            result = max(result, freq)

        return max(result, freq)


# print(Solution().maxFrequency(nums=[1, 4, 8, 13], k=5))
# print(Solution().maxFrequency(nums=[1, 2, 4], k=5))

# Sliding Window technique:


class Solution2:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        windowlength = 1
        total = 0
        while r < len(nums):
            total += nums[r]
            while (r-l+1)*nums[r] > total+k:
                total -= nums[l]
                l += 1
            windowlength = max(windowlength, r-l+1)
            r += 1

        return windowlength


print(Solution2().maxFrequency(nums=[1, 4, 8, 13], k=5))
print(Solution2().maxFrequency(nums=[1, 2, 4], k=5))
