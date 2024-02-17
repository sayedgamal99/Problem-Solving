from queue import PriorityQueue


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        pq = PriorityQueue()

        for i in range(len(heights)-1):
            d = heights[i+1]-heights[i]
            if d <= 0:
                continue
            bricks -= d
            pq.put(-d)
            if bricks < 0:
                bricks += -pq.get()
                ladders -= 1
            if ladders < 0:
                return i
        return len(heights)-1


print(Solution().furthestBuilding(
    heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(Solution().furthestBuilding(
    heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
print(Solution().furthestBuilding([1, 5, 1, 2, 3, 4, 10000], 4, 1))
