# Accepted Solution but not efficient
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        themap1 = Counter(s1)
        for r in range(len(s2)):
            if s2[r] in themap1:
                if (r+len(s1)) <= len(s2) and Counter(s2[r:r+len(s1)]) == themap1:
                    return True
        return False

# print(Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo"))

# better Accepted solution:


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        themap1 = Counter(s1)
        themap2 = Counter(s2[:len(s1)])

        if themap1 == themap2:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            themap2[s2[i - 1]] -= 1
            if themap2[s2[i - 1]] == 0:
                del themap2[s2[i - 1]]
            themap2[s2[i + len(s1) - 1]] += 1

            if themap1 == themap2:
                return True

        return False


# print(Solution2().checkInclusion(s1="ab", s2="eidbaooo"))
print(Solution2().checkInclusion(s1="adc", s2="dcda"))
