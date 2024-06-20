from math import ceil


class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        answer = 0
        n = len(position)
        low = 1
        high = position[-1] - position[0]

        while low <= high:
            mid = (low + high) // 2
            if self.canPlaceBalls(mid, position, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer

    def canPlaceBalls(self, x, position, m):
        prevBallPos = position[0]
        ballsPlaced = 1
        for i in range(1, len(position)):
            if position[i] - prevBallPos >= x:
                prevBallPos = position[i]
                ballsPlaced += 1
                if ballsPlaced == m:
                    return True
        return False
