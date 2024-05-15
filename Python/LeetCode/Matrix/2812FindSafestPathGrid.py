from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        N = len(grid)

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def precompute():
            q = deque()
            min_dist = {}
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for r2, c2 in nei:
                    if in_bounds(r, c) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist+1])
            return min_dist

        min_dist = precompute()

        max_heap = [(-min_dist[(0, 0)], 0, 0)]  # dist, r, c
        visit = set()
        visit.add((0, 0))

        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = -dist
            if (r, c) == (N - 1, N - 1):
                return dist

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r2, c2 = r + dr, c + dc
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    dist2 = min(min_dist[(r2, c2)], dist)
                    heapq.heappush(max_heap, (-dist2, r2, c2))


print(Solution().maximumSafenessFactor(
    grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))  # 2
