from collections import Counter as CO


class Solution:
    def uniquePalindrom(self, s):
        res = set()
        left = set()
        right = CO(s)
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            for j in range(26):
                c = chr(97+j)
                if c in left and c in right:
                    res.add((s[i], c))

            left.add(s[i])

        return len(res)


s = 'fafaazmae'
# s = 'aabca'
print(Solution().uniquePalindrom(s))
