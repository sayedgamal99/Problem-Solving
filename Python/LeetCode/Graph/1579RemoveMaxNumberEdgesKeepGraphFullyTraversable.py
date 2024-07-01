class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice, bob = UF(n), UF(n)
        cnt = 0
        for t, u, v in edges:
            if t == 3:
                cnt += (alice.union(u, v) | bob.union(u, v))

        for t, u, v in edges:

            if t == 1:
                cnt += alice.union(u, v)
            elif t == 2:
                cnt += bob.union(u, v)

        if bob.isConnected() and alice.isConnected():
            return len(edges)-cnt
        return -1
