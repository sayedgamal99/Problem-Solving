# O(n) solution:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        completerows = 0
        nn = n
        for i in range(1, n+1):
            nn -= i
            if nn >= 0:
                completerows += 1
            else:
                return completerows
        return completerows

# better solution O(log(n)):


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while l <= r:
            mid = (l+r)//2
            co = (mid/2)*(mid+1)
            if co > n:
                r = mid-1
            else:
                l = mid+1
                res = max(res, mid)
        return res


# best solution O(1) with math
"""
solution come from fact that sum of numbers from 1 to n = n/2 * (n+1)
let complete rows are donated by K
coins that complete these K rows are K/2 * (K+1) = (K^2)/2 + K/2 >> X
we garmented that n coins bigger than that summation  X

(K^2)/2 + K/2 <= n
(K^2) + K <= 2n
(K^2) + K -2n <= 0
solving this equation for K will give us number of complete rows directly.
ax^2 +bx +c =0
from the formula of k = -b + sqrt(b^2 - 4ac)/2a
k = -1 + sqrt(1-4*1*-2n)/2 >> -1 + sqrt(1+8n)/2

"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8*n) ** 0.5) // 2)
