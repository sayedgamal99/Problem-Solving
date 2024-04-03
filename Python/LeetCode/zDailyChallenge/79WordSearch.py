from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if (Counter(word) - Counter([i[j] for i in board for j in range(n)])):
            return False

        def dfs(i, j, k, visited=set()):
            if not (0 <= i < m) or not (0 <= j < n) or ((i, j) in visited) or board[i][j] != word[k]:
                return False

            visited.add((i, j))
            if k == (len(word)-1):
                return True

            found = (dfs(i+1, j, k+1, visited) or
                     dfs(i, j+1, k+1, visited) or
                     dfs(i-1, j, k+1, visited) or
                     dfs(i, j-1, k+1, visited))
            visited.remove((i, j))
            return found

        for ii in range(m):
            for jj in range(n):
                if dfs(ii, jj, 0):
                    return True
        return False


print(Solution().exist(board=[["A", "B", "C", "E"],
                              ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="ABCCED"))  # Output: True

print(Solution().exist(board=[["A", "B", "C", "E"],
                              ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="SEE"))     # Output: True

print(Solution().exist(board=[["A", "B", "C", "E"],
                              ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="ABCB"))    # Output: False
