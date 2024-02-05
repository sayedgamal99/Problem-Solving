class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        themap = {}
        result = 0
        max_count = 0

        for r in range(len(s)):
            themap[s[r]] = themap.get(s[r], 0) + 1
            max_count = max(max_count, themap[s[r]])

            if (r - l + 1) - max_count <= k:
                result = max(result, r - l + 1)
            else:
                themap[s[l]] -= 1
                l += 1

        return result


print(Solution().characterReplacement(s="AABABBA", k=1))
print(Solution().characterReplacement(s="AABABBA", k=2))
