class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0]*38
        tri[0] = 0
        tri[1] = 1
        tri[2] = 1
        for t in range(3, n+1):
            tri[t] = tri[t-1]+tri[t-2]+tri[t-3]
        return tri[n]


print(Solution().tribonacci(25))
