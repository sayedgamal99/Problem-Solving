from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        themap = Counter(arr)
        sortedmap = sorted(themap.items(), key=lambda x: x[1])
        for key, v in sortedmap:
            if v > k:
                break
            k -= v
            themap.pop(key)

        return len(themap)


# print(Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
print(Solution().findLeastNumOfUniqueInts([5, 5, 4], 1))
