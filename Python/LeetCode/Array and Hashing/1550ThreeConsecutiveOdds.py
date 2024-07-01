class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        odds = 0
        for a in arr:
            if a % 2:
                odds += 1
            else:
                odds = 0
            if odds > 2:
                return True
        return False
