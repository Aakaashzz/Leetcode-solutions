class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]

        @cache
        def calc(i, j, cur, prob):
            if not (0 <= i < n) or not (0 <= j < n):
                return 0

            if not cur:
                return prob

            best = 0
            for ii, jj in directions:
                best += calc(i + ii, j + jj, cur - 1, prob * 1 / 8)


            return best


        return calc(row, column, k, 1)
