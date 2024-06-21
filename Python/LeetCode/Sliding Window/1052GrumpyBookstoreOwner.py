from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        masked = [0]*n

        sum_masked = 0
        sum_customer = 0
        for i in range(n):
            masked[i] = grumpy[i]*customers[i]
            sum_masked += masked[i]
            sum_customer += customers[i]

        maximized_sliding = 0
        sum_temp = 0
        l = 0
        for r in range(n):
            sum_temp += masked[r]
            if r-l+1 > minutes:
                sum_temp -= masked[l]
                l += 1

            maximized_sliding = max(maximized_sliding, sum_temp)
        answer = sum_customer-sum_masked+maximized_sliding
        return answer


print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[
      0, 1, 0, 1, 0, 1, 0, 1], minutes=3))  # 16

print(Solution().maxSatisfied(customers=[4, 10, 10], grumpy=[
      1, 1, 0], minutes=2))  # 24
