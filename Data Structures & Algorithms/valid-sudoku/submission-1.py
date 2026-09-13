class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # 1 goes to bit 0, 2 goes to bit 1, etc. 
                idx = int(board[r][c]) - 1
                mask = 1 << idx

                # check if the bit is already set
                if mask & rows[r]:
                    return False
                if mask & cols[c]:
                    return False
                if mask & squares[r // 3 * 3 + c // 3]:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[r // 3 * 3 + c // 3] |= mask

        return True



