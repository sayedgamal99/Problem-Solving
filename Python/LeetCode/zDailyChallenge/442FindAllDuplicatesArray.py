class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        theset = set()
        duplicates = set()
        for n in nums:
            if n in theset:
                duplicates.add(n)
            theset.add(n)
        return list(duplicates)
