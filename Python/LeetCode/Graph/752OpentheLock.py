from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+1) % 10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i])-1+10) % 10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        visited = set(deadends)
        q = deque()  # lock, turns
        q.append(["0000", 0])
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, turns+1])

        return -1


print(Solution().openLock(
    deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))



"""
main idea is to assume that string 'lock' is a node in graph with all 
values from 0000 to 9999 (10000 values) are nodes between them edges (increment by 1 or decrement by 1)
except the dead ends, so we need to EXPLORE that graph to find (minimum = shortestPath = BFS).

"""