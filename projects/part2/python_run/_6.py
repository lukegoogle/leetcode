class Solution:
    def convert(self, s: str, numRows: int) -> str:
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
    
sol = Solution()
print("--- Zigzag Conversion Examples ---")
    
# Test Case 1: Standard Example (numRows=3)
# P   A   H   N
# A P L S I I G
# Y   I   R
s1 = "PAYPALISHIRING"
numRows1 = 3
result1 = sol.convert(s1, numRows1)
# Expected: "PAHNAPLSIIGYIR"
print(f"Input: s='{s1}', numRows={numRows1}")
print(f"Output: '{result1}' (Expected: 'PAHNAPLSIIGYIR')")

# Test Case 2: Example with 4 rows
# P     I     N
# A   L S   I G
# Y A   H R
# P     I
s2 = "PAYPALISHIRING"
numRows2 = 4
result2 = sol.convert(s2, numRows2)
# Expected: "PINALSIGYAHRPI"
print(f"Input: s='{s2}', numRows={numRows2}")
print(f"Output: '{result2}' (Expected: 'PINALSIGYAHRPI')")
# 
    
# Test Case 3: Simple 2-row case
s3 = "ABCDEFGH"
numRows3 = 2
result3 = sol.convert(s3, numRows3)
# Expected: "ACEGBDFH"
print(f"Input: s='{s3}', numRows={numRows3}")
print(f"Output: '{result3}' (Expected: 'ACEGBDFH')")
    
# Test Case 4: numRows = 1 (Edge Case)
s4 = "ABCDE"
numRows4 = 1
result4 = sol.convert(s4, numRows4)
# Expected: "ABCDE"
print(f"Input: s='{s4}', numRows={numRows4}")
print(f"Output: '{result4}' (Expected: 'ABCDE')")
    
# Test Case 5: numRows >= len(s) (Edge Case)
s5 = "ABC"
numRows5 = 5
result5 = sol.convert(s5, numRows5)
# Expected: "ABC"
print(f"Input: s='{s5}', numRows={numRows5}")
print(f"Output: '{result5}' (Expected: 'ABC')")