class Solution2:
    def findCenter(self, edges: list[list[int]]) -> int:
        return set([*edges[0]]).intersection(set([*edges[1]])).pop()


class Solution1:
    def findCenter(self, edges: list[list[int]]) -> int:
        theset = set([*edges[0]])
        for u, v in edges[1:]:
            theset = theset.intersection(set([u, v]))
        return theset.pop()


print(Solution2().findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
print(Solution1().findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
