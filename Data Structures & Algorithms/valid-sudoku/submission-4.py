class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 hashmaps with a set as the value, rows, cols, 3x3 squares
        # each 3x3 is turned into rows and cols 0, 1, 2 for indexing
        # use the coordinate index as the keys
        # squares are found with row // 3, col // 3
        # skip if no number "."

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