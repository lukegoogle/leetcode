class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a given string into a zigzag pattern and then reads it line by line.

        The method simulates the zigzag writing process by maintaining a list of 
        strings, where each string represents a row in the final pattern. 
        It iterates through the input string $s$, appending each character to 
        the correct row.

        A direction flag (`going_down`) and a current row index (`current_row`) 
        are used to manage the movement:
        1. When the index reaches row 0 or row `numRows - 1`, the direction reverses.
        2. The row index is incremented (down) or decremented (up) based on the 
           current direction.

        Finally, the characters from all rows are concatenated to form the 
        final converted string.

        Args:
            s: The string to be converted.
            numRows: The number of rows for the zigzag pattern.

        Returns:
            The converted string.

        Examples:
            If $s = "PAYPALISHIRING"$ and $numRows = 3$:
            
            P   A   H   N
            A P L S I I G
            Y   I   R
            
            The result is "PAHNAPLSIIGYIR".

            >>> sol = Solution()
            >>> sol.convert("PAYPALISHIRING", 3)
            'PAHNAPLSIIGYIR'
            >>> sol.convert("PAYPALISHIRING", 4)
            'PINALSIGYAHRPI'
            >>> sol.convert("A", 1)
            'A'
        """
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)