class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 0
        profit = 0
        max_profit = 0
        i = 0
        while i < len(prices):
            if prices[i] < prices[buy]:
                buy = i
                sell = i+1 if i+1 < len(prices) else i
            if prices[i] > prices[sell]:
                sell = i
            profit = prices[sell]-prices[buy]
            if profit > max_profit:
                max_profit = profit
            i += 1

        return max_profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 1, 4, 3, 6]))
