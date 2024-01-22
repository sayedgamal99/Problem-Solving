class Solution:
    def maxProduct(self, s: str) -> int:
        N,themap = len(s),{}
        for mask in range(1,1<<N):# 1<<N as same as 2^N
            subsequance = ''
            for i in range(N):
                if (1<<i) & mask:
                    subsequance+=s[N-1-i]
            if subsequance == subsequance[::-1]:
                themap[mask] = len(subsequance)
        
        result = 0
        for m in themap:
            for n in themap:
                if m & n == 0 :
                    result = max(result,themap[m]*themap[n])
        return result









S = input()
print(Solution().maxProduct(S))