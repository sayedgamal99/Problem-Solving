from collections import defaultdict


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Count connections for each node
        nodes_connections = defaultdict(int)
        for u, v in roads:
            nodes_connections[u] += 1
            nodes_connections[v] += 1

        # Step 2: Assign importance values to nodes based on their connection counts
        importance_dict = {}
        for v in sorted(nodes_connections, key=nodes_connections.get, reverse=True):
            importance_dict[v] = n
            n -= 1

        # Step 3: Calculate the total importance of all roads
        answer = 0
        for u, v in roads:
            answer += (importance_dict[u] + importance_dict[v])

        return answer


# Testing the solution
test1 = Solution().maximumImportance(
    n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
test2 = Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]])

assert test1 == 43, f"Wrong Answer, should be 43 not {test1}"
assert test2 == 20, f"Wrong Answer, should be 20 not {test2}"

print("All tests passed")
