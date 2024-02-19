class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return bin(n)[2:].count('1') == 1


print(Solution().isPowerOfTwo(16))
