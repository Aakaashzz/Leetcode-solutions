class Solution:
    def totalNQueens(self, n: int) -> int:
        @cache
        def attack(r: int, positions: frozenset[Tuple[int]]) -> int:
            if r == 1:
                return len(positions)
            return sum(
                attack(r - 1, positions - attacked(i, j))
                for i, j in positions
            )

        @cache
        def attacked(i: int, j: int) -> FrozenSet[Tuple[int]]:
            domain = range(i + 1, n)
            return frozenset(chain(
                product(range(i + 1), range(n)),
                zip(domain, repeat(j)),
                zip(domain, range(j + 1, n)),
                zip(domain, reversed(range(j))),
            ))

        return attack(n, frozenset(product(range(n), repeat=2)))