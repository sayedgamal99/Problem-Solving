class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 0
        r = num//2

        while l <= r:
            mid = l + (r-l)//2
            midsquare = mid*mid
            if midsquare == num:
                return True
            elif midsquare < num:
                l = mid+1
            else:
                r = mid-1
        return False
