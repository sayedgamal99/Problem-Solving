from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        themap = Counter(s)
        for i, ch in enumerate(s):
            if themap[ch] == 1:
                return i


print(Solution().firstUniqChar('leetcode'))
