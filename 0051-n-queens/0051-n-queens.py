class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = [] 

        board = [['.'] *n for _ in range(n)]
        
        col_bag = set()
        pos_dia_bag = set()
        neg_dia_bag =set()

        def place_queens(r):

            if r == n:
                solution = ["".join(row) for row in board]
                ans.append(solution)
                return

            for col in range(n):
                pos_dia = r+col
                neg_dia = r-col

                if col in col_bag or pos_dia in pos_dia_bag or neg_dia in neg_dia_bag:
                    continue

                board[r][col] = 'Q'
                col_bag.add(col)
                pos_dia_bag.add(pos_dia)
                neg_dia_bag.add(neg_dia)

                place_queens(r+1)

                # redoing all the changes
                board[r][col] = '.'
                col_bag.remove(col)
                pos_dia_bag.remove(pos_dia)
                neg_dia_bag.remove(neg_dia)


        place_queens(0)

        return ans


