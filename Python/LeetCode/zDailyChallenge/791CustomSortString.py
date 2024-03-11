# ACCEPTED
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        themap = {}
        for i, letter in enumerate(order):
            themap[letter] = i
        i = len(order)
        for j in range(len(s)):
            if s[j] not in themap:
                themap[s[j]] = i+j

        return sorted(s, key=lambda x: themap[x])


# print(Solution().customSortString(order="cba", s="abccd"))

# another solution using also map and counting:
from collections import Counter
class Solution2:
    def customSortString(self, order, s):
        themap = Counter(s)
        answer= []
        for i in order:
            if i in themap:
                answer.append(i*themap[i])
                del themap[i]

        for k,v in themap.items():
            answer.append(k*v)
        return ''.join(answer)


print(Solution2().customSortString(order="cba", s="abccd"))
