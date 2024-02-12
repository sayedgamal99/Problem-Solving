class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        maxi = 0
        vo = 0
        for r in range(len(s)):
            if s[r] in vowels:
                vo += 1
            if r >= k:
                if s[l] in vowels:
                    vo -= 1
                l += 1

            maxi = max(maxi, vo)

        return maxi


print(Solution().maxVowels(s="abciiidef", k=3))
print(Solution().maxVowels(s="leetcode", k=3))
