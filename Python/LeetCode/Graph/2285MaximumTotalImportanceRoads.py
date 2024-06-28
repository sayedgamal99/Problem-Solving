from collections import defaultdict


class SolutionOptimized:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Count the number of connections (roads) for each node
        edge_counts = [0] * n
        for u, v in roads:
            edge_counts[u] += 1
            edge_counts[v] += 1

        # Step 2: Sort the connection counts
        sorted_counts = sorted(edge_counts)

        # Step 3: Calculate the total importance
        answer = 0
        label = 1
        for count in sorted_counts:
            answer += label * count
            label += 1

        return answer


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
test1 = SolutionOptimized().maximumImportance(
    n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
test2 = SolutionOptimized().maximumImportance(
    n=5, roads=[[0, 3], [2, 4], [1, 3]])

assert test1 == 43, f"Wrong Answer, should be 43 not {test1}"
assert test2 == 20, f"Wrong Answer, should be 20 not {test2}"

print("All tests passed")
