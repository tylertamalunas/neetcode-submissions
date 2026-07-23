class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need 3 hashmaps with hashset values and the key is the location on sudoku grid
        # squares are broken down into 0, 1, 2, by using integer division r // ,3 c // 3
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True