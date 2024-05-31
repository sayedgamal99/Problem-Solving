class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        theset = set()
        for n in nums:
            if n in theset:
                theset.remove(n)
            else:
                theset.add(n)
        return list(theset)
