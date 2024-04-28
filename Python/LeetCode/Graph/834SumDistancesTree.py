from collections import defaultdict, deque


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        output = [0]*n
        count = [1]*n
        self.root = 0

        def dfs(cur, parent, depth):
            o = 1
            for child in graph[cur]:
                if child != parent:
                    o += dfs(child, cur, depth+1)
                    self.root += depth+1
            count[cur] = o
            return o
        dfs(0, -1, 0)

        def dfs2(cur, parent, ans_p):
            output[cur] = ans_p
            for child in graph[cur]:
                if child != parent:
                    dfs2(child, cur, ans_p+(n-2*count[child]))
        dfs2(0, -1, self.root)

        return output


class SolutionTLE:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:

        graph = self.edgesToGraph(edges)

        def travel(i):
            visited = set([i])
            q = deque([(i, 0)])
            output = 0
            while q:
                cur, dis = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dis+1))
                        output += (dis+1)
            return output

        return [travel(i) for i in range(n)]

    def edgesToGraph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph


print('TLE Solution: ', SolutionTLE().sumOfDistancesInTree(
    n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))

print('Solution: ', Solution().sumOfDistancesInTree(
    n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
