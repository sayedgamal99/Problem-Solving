class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        xor = 0
        for n in nums:
            xor = xor ^ n
        xor ^= k
        xor = str(bin(xor)[2:])
        # print(xor)
        return xor.count('1')


print(Solution().minOperations(nums=[2, 1, 3, 4], k=1))
