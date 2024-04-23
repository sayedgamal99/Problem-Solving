from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        thegraph = defaultdict(list)
        for u, v in edges:
            thegraph[u].append(v)
            thegraph[v].append(u)

        edge_cnt = {}
        leaves = deque()

        for root, neighbors in thegraph.items():
            if len(neighbors) == 1:
                leaves.append(root)
            edge_cnt[root] = len(neighbors)

        while leaves:

            if n <= 2:
                return list(leaves)

            for _ in range(len(leaves)):
                node = leaves.popleft()

                n -= 1
                for nei in thegraph[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(
    6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))


class SolutionTLE:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        thegraph = self.edgesToGraph(edges)
        MHT = defaultdict(list)
        for t in thegraph:

            q = deque()
            q.append([t, 0])
            visited = set()
            visited.add(t)

            while q:
                root, height = q.popleft()
                for child in thegraph[root]:
                    if child not in visited:
                        visited.add(child)
                        q.append([child, height+1])
            MHT[height].append(t)

        return MHT[min(MHT)]

    def edgesToGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph


# print(SolutionTLE().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
# print(SolutionTLE().findMinHeightTrees(
#     6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
