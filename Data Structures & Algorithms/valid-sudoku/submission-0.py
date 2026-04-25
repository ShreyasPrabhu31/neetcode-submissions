class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #Hash set to check for duplicates in rows
        cols = collections.defaultdict(set) #Hash set to check for duplicates in cols
        squares = collections.defaultdict(set) #Hash set to check for duplicates in 3x3 grids

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # To check if the value in the board is already present in the hash sets to find out duplicates
                if (board[r][c] in rows[r] 
                   or board[r][c] in cols[c]
                   or board[r][c] in squares[(r // 3, c // 3)]):
                   return False
                # To add the values found in the iteration to rows, cols or the grids if they are not found
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

        