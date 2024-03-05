class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n-1
        while l < r:
            right, left = s[r], s[l]
            entered = False
            while l <= r and (s[l] == left == right):
                l += 1
                entered = True
            while l <= r and (s[r] == right == left):
                r -= 1
                entered = True
            if not entered:
                break

        res = r-l
        return res+1


print(Solution().minimumLength("cabaabac"))
print(Solution().minimumLength("ca"))
print(Solution().minimumLength("aabccabba"))
