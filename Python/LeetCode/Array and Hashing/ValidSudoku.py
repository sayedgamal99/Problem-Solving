import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]] ) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if( board[r][c] in cols[c] or 
                    board[r][c] in rows[r] or
                    board[r][c] in square[(r//3,c//3)]):
                    

                    # print(cols,rows,square,sep='\n\n')
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        print(cols,rows,square)
        return True
                


board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","0",".",".",".",".","6","."]
,["2",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
