class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for n in nums:
            xor ^= n

        diff_bit = 1
        while not (diff_bit & xor):
            diff_bit = diff_bit << 1
        a, b = 0, 0
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n

        return [a, b]
