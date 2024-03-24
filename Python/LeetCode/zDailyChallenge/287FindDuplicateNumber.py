class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        theset = set()
        for n in nums:
            if n in theset:
                return n
            theset.add(n)
        return -1
