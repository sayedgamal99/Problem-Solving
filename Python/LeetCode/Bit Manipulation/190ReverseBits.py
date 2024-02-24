class Solution:
    def reverseBits(self, n: int) -> int:
        rr = bin(n)[2:].zfill(32)
        return int(rr[::-1], 2)
