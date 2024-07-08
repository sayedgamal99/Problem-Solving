class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i+1 for i in range(n)]
        start = 0
        while len(queue) > 1:
            toPop = (start+k-1) % n
            queue.pop(toPop)
            start = toPop
            n -= 1
        return queue[0]


print(Solution().findTheWinner(5, 2))  # 3
print(Solution().findTheWinner(6, 5))  # 1
