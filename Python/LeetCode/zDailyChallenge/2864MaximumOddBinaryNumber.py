class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        result = '1'*(ones-1) + '0'*(len(s)-ones) + '1'
        return result


print(Solution().maximumOddBinaryNumber('0101'))
"""
Input: s = "0101"
Output: "1001"
"""
