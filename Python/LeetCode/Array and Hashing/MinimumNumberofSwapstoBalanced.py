
class Solution:
    def minSwaps(self, s: str) -> int:
        import math
        closing,maxi = 0,-math.inf
        for ch in s:
            if ch == ']' :
                closing+=1
            else:
                closing-=1
            maxi = max(closing,maxi)
        return (maxi+1)//2

s = input()
print(Solution().minSwaps(s))