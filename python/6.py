def convert(s: str, numRows: int) -> str:
    if numRows == 1 or len(s) <= numRows:
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        # Change direction at the top and bottom rows
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
            
        # Update row index based on direction
        if going_down:
            current_row += 1
        else:
            current_row -= 1
            
    # Join the rows to form the final string
    return "".join(rows)