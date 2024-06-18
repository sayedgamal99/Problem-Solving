from bisect import bisect_right


class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        n = len(difficulty)
        temp = sorted(zip(difficulty, profit))
        difficulty, profit = map(list, zip(*temp))

        maxProfit = [0] * n
        maxProfit[0] = profit[0]

        for i in range(1, n):
            maxProfit[i] = max(maxProfit[i - 1], profit[i])

        answer = 0
        for w in worker:
            idx = bisect_right(difficulty, w) - 1
            if idx >= 0:
                answer += maxProfit[idx]

        return answer
