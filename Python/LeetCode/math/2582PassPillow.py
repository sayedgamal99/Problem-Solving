class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        fullRounds = time // (n-1)
        extra = time % (n-1)

        if fullRounds % 2 == 0:
            return extra + 1
        else:
            return n - extra


print(Solution().passThePillow(4, 5))
print(Solution().passThePillow(3, 2))
