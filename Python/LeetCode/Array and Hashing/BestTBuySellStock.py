"""
You can buy and sell in the same day.
"""
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1] :
                profit +=(prices[i-1]-buy)
                buy = prices[i]
            
        if prices[-1]>buy:
            profit+=(prices[-1]-buy)
        return profit


A = [7,1,5,3,6,4]
print(Solution().maxProfit(A))

            

"""

"""
You can buy single share and sell it once, only one transaciton.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pre =[0]
        for i in range(1,len(prices)):
            pre.append(prices[i]-prices[i-1])
        
        maxprofit = -9999
        sum=0
        for i in range(len(pre)):
            sum+=pre[i]
            if sum>maxprofit:
                maxprofit = sum
            if sum<0:
                sum=0
                


            
        return maxprofit


A = [7,1,5,3,6,4]
print(Solution().maxProfit(A))

            

