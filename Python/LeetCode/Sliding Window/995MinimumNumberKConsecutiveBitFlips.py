from collections import deque


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        q = deque()
        flips = 0
        for i in range(n):
            while q and i > q[0] + k - 1:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:
                if i + k > n:
                    return -1
                flips += 1
                q.append(i)
        return flips


print(Solution().minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))
print(Solution().minKBitFlips(nums=[1, 1, 0], k=2))
print(Solution().minKBitFlips(nums=[0, 1, 0], k=1))
