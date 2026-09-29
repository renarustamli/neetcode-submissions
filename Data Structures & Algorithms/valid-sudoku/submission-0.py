class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in board:
            row = set()
            for j in range(0,9):
                if i[j] != "." and i[j] in row:
                    return False
                elif i[j] != ".":
                    row.add(i[j])
        for i in range(0,9):
            column = set()
            for j in board:
                if j[i] != "." and j[i] in column:
                    return False
                elif j[i] != ".":
                    column.add(j[i])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True