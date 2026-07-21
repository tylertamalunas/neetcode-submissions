class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use of hashmap and sets
        # set each 3x3 to be its own index, (0, 1, 2) vertical and horiz
        # need to make 3 hash maps, (rows, cols, squares)
        # treat each box on board as coordinates
        # squares coords found with (row//3, col//3)
        # keys are index, values are the number
        # 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3), (j // 3)]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3),(j // 3)].add(board[i][j])
        
        return True