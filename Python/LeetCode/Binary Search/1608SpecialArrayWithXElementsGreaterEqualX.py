from bisect import bisect_left, bisect_right, bisect


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = -1
        for x in range(n+1):
            idx = bisect_left(nums, x)
            print(idx, n-idx, x)
            if (n - idx) == x:
                answer = max(n-idx, answer)
        return answer


print(Solution().specialArray(nums=[0, 4, 3, 0, 4]))  # 0 0 3 4 4
print(Solution().specialArray(nums=[0, 0]))
print(Solution().specialArray(nums=[3, 5]))
