class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVals = defaultdict(set)
        colVals = defaultdict(set)
        squareVals = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowVals[row]
                or board[row][col] in colVals[col]
                or board[row][col] in squareVals[(row // 3, col // 3)]):
                    return False

                rowVals[row].add(board[row][col])
                colVals[col].add(board[row][col])
                squareVals[(row // 3, col // 3)].add(board[row][col])
        
        return True