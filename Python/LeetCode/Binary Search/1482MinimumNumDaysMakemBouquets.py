from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # If it's impossible to form the required number of bouquets
        if m * k > len(bloomDay):
            return -1

        # Binary search boundaries
        left, right = 1, max(bloomDay)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if self.canMakeBouquets(bloomDay, mid, m, k):
                answer = mid  # Update answer to the current valid day
                right = mid - 1  # Try for fewer days
            else:
                left = mid + 1  # Need more days

        return answer

    def canMakeBouquets(self, bloomDay: List[int], day: int, m: int, k: int) -> bool:
        bouquets = 0
        flowers = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0  # Reset count if the flower hasn't bloomed in the given days

            if bouquets >= m:
                return True

        return bouquets >= m
