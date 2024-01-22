class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        hashmap ,maxxi= {},0
        for row in wall:
            prev = 0
            for position in row[:-1]:
                prev+=position
                hashmap[prev] = hashmap.get(prev,0)+1
                maxxi = max(maxxi,hashmap[prev])

        return len(wall)-maxxi

        






wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(Solution().leastBricks(wall=wall))
"""
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

"""