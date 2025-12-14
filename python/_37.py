class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        
        def is_valid(r, c, val):
            for i in range(9):
                if board[r][i] == val or board[i][c] == val:
                    return False
            
            start_r, start_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_r + i][start_c + j] == val:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val_char in "123456789":
                            if is_valid(r, c, val_char):
                                board[r][c] = val_char
                                if backtrack():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
            
        backtrack()

# --- Example Usage Code ---

sol = Solution()
print("--- Sudoku Solver Examples ---")

# Test Case 1: Standard Sudoku puzzle
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print("Input Board:")
for row in board1:
    print(row)

sol.solveSudoku(board1)

print("\nOutput Solved Board:")
# Expected solved board:
# ['5', '3', '4', '6', '7', '8', '9', '1', '2']
# ['6', '7', '2', '1', '9', '5', '3', '4', '8']
# ['1', '9', '8', '3', '4', '2', '5', '6', '7']
# ['8', '5', '9', '7', '6', '1', '4', '2', '3']
# ['4', '2', '6', '8', '5', '3', '7', '9', '1']
# ['7', '1', '3', '9', '2', '4', '8', '5', '6']
# ['9', '6', '1', '5', '3', '7', '2', '8', '4']
# ['2', '8', '7', '4', '1', '9', '6', '3', '5']
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']
for row in board1:
    print(row)