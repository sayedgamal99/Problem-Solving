from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def todict(thelist):
            graph = defaultdict(list)
            for u, v in thelist:
                graph[u].append(v)
                graph[v].append(u)
            return graph
        edges = todict(edges)

        visited = set()

        def dfs(currentNode):
            if currentNode == destination:
                return True
            visited.add(currentNode)
            for neighbor in edges[currentNode]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)


print(Solution().validPath(n=3, edges=[
      [0, 1], [1, 2], [2, 0]], source=0, destination=2))
