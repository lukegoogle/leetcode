class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # 1. Initialize constraint sets
        # row_constraints[r] is a set of digits present in row r
        row_constraints = [set() for _ in range(9)]
        # col_constraints[c] is a set of digits present in column c
        col_constraints = [set() for _ in range(9)]
        # box_constraints[b] is a set of digits present in box b (where b is 0-8)
        # The box index b can be calculated as b = (r // 3) * 3 + (c // 3)
        box_constraints = [set() for _ in range(9)]
        
        # 2. Pre-fill the constraints and collect empty cells
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    row_constraints[r].add(val)
                    col_constraints[c].add(val)
                    box_constraints[box_idx].add(val)
                else:
                    empty_cells.append((r, c))

        # 3. Optimized validity check (O(1))
        def is_valid_optimized(r, c, val):
            box_idx = (r // 3) * 3 + (c // 3)
            return (val not in row_constraints[r] and
                    val not in col_constraints[c] and
                    val not in box_constraints[box_idx])

        # 4. Backtracking with constraint updates
        def backtrack(k):
            # Base case: All empty cells have been filled
            if k == len(empty_cells):
                return True

            r, c = empty_cells[k]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Iterate through possible values '1' to '9'
            for val_char in "123456789":
                if is_valid_optimized(r, c, val_char):
                    
                    # Place the value and update constraints
                    board[r][c] = val_char
                    row_constraints[r].add(val_char)
                    col_constraints[c].add(val_char)
                    box_constraints[box_idx].add(val_char)
                    
                    # Recurse to the next empty cell
                    if backtrack(k + 1):
                        return True
                    
                    # Backtrack: Reset the cell and constraints
                    board[r][c] = '.'
                    row_constraints[r].remove(val_char)
                    col_constraints[c].remove(val_char)
                    box_constraints[box_idx].remove(val_char)
            
            # If no value works for this cell, return False
            return False

        # Start backtracking from the first empty cell
        backtrack(0)

# --- Example Usage Code ---
# (The usage code remains the same, just replace 'Solution' with 'SolutionOptimized')

sol = Solution()
print("--- Sudoku Solver Examples (Optimized) ---")

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

print("\nOutput Solved Board (Optimized):")
for row in board1:
    print(row)