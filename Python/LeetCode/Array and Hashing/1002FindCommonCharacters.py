from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        for w in words:
            current = Counter(w)
            for c in common:
                common[c] = min(common[c], current[c])
        res = []
        for c in common:
            res.extend([c] * common[c])
        return res


words = ["bella", "label", "roller"]
print(Solution().commonChars(words))
