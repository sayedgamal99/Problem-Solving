from collections import defaultdict


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:

        # Initialize adjacency list and ancestors list
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        def dfs(node, ancestors, visited):
            for ancestor in graph[node]:
                if ancestor not in visited:
                    visited.add(ancestor)
                    ancestors.add(ancestor)
                    dfs(ancestor, ancestors, visited)

        result = [[] for _ in range(n)]

        for node in range(n):
            ancestors = set()
            visited = set()
            dfs(node, ancestors, visited)
            result[node] = sorted(ancestors)

        return result


test1 = Solution().getAncestors(n=8, edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [
    3, 6], [3, 7], [4, 6]])
Output = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
test2 = Solution().getAncestors(n=5, edges=[[0, 1], [0, 2], [0, 3], [
    0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
Output2 = [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
assert test1 == Output, 'Wrong Answer test1'
assert test2 == Output2, 'Wrong Answer test2'

print('all tests passed!')
