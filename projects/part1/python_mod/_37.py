class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        row_constraints = [set() for _ in range(9)]
        col_constraints = [set() for _ in range(9)]
        box_constraints = [set() for _ in range(9)]
        
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

        def is_valid_optimized(r, c, val):
            box_idx = (r // 3) * 3 + (c // 3)
            return (val not in row_constraints[r] and
                    val not in col_constraints[c] and
                    val not in box_constraints[box_idx])

        def backtrack(k):
            if k == len(empty_cells):
                return True

            r, c = empty_cells[k]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for val_char in "123456789":
                if is_valid_optimized(r, c, val_char):
                    
                    board[r][c] = val_char
                    row_constraints[r].add(val_char)
                    col_constraints[c].add(val_char)
                    box_constraints[box_idx].add(val_char)
                    
                    if backtrack(k + 1):
                        return True
                    
                    board[r][c] = '.'
                    row_constraints[r].remove(val_char)
                    col_constraints[c].remove(val_char)
                    box_constraints[box_idx].remove(val_char)
            
            return False

        backtrack(0)
