from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        co = Counter(s)
        result = 0
        odd_found = False
        for count in co.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                odd_found = True
        if odd_found:
            result += 1
        return result
