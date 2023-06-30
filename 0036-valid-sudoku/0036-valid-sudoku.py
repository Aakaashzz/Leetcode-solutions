"""https://leetcode.com/problems/valid-sudoku/"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for i in range(9):
            for c in range(9):
                if board[i][c] == ".":
                    continue
                if (
                    board[i][c] in rows[i]
                    or board[i][c] in cols[c]
                    or board[i][c] in squares[(i // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[i][c])
                rows[i].add(board[i][c])
                squares[(i // 3, c // 3)].add(board[i][c])

        return True
                