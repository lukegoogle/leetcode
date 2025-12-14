class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                
                if char in rows[r] or char in cols[c] or char in boxes[box_index]:
                    return False
                
                rows[r].add(char)
                cols[c].add(char)
                boxes[box_index].add(char)
                
        return True
    
# --- Example Usage Code ---

sol = Solution()
print("--- Valid Sudoku Examples ---")

# Test Case 1: Valid board (Partial fill, but valid structure)
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
result1 = sol.isValidSudoku(board1)
print("Test 1 (Valid):")
print(f"Output: {result1} (Expected: True)")


# Test Case 2: Invalid board (Duplicate in a row)
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
] # Row 0 has '8' and row 3 has '8' at col 0, which is fine.
# Let's create a clear row violation:
board2_row_violation = [
    ["8", "8", ".", ".", "7", ".", ".", ".", "."],  # Duplicate '8' in row 0
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result2 = sol.isValidSudoku(board2_row_violation)
print("\nTest 2 (Row Violation):")
print(f"Output: {result2} (Expected: False)")


# Test Case 3: Invalid board (Duplicate in a 3x3 box)
board3_box_violation = [
    ["5", "3", ".", "1", "7", ".", ".", ".", "."],
    ["6", "1", ".", "1", "9", "5", ".", ".", "."], # Duplicate '1' in box 0 (0,0 to 2,2)
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result3 = sol.isValidSudoku(board3_box_violation)
print("\nTest 3 (Box Violation):")
print(f"Output: {result3} (Expected: False)")