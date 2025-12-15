class Solution:
    def romanToInt(self, s: str) -> int:
        
        value_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = value_map[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
            
        return total
    
# --- Example Usage Code ---

sol = Solution()
print("--- Roman to Integer Examples ---")

# Test Case 1: Simple addition
s1 = "III"
result1 = sol.romanToInt(s1)
print(f"Input: '{s1}'")
print(f"Output: {result1} (Expected: 3)")

# Test Case 2: Subtractive notation (IV = 5 - 1 = 4)
s2 = "IV"
result2 = sol.romanToInt(s2)
print(f"Input: '{s2}'")
print(f"Output: {result2} (Expected: 4)")

# Test Case 3: Subtractive notation (IX = 10 - 1 = 9)
s3 = "IX"
result3 = sol.romanToInt(s3)
print(f"Input: '{s3}'")
print(f"Output: {result3} (Expected: 9)")

# Test Case 4: Mixed addition and subtraction
s4 = "LVIII"
# L (50) + V (5) + I (1) + I (1) + I (1) = 58
result4 = sol.romanToInt(s4)
print(f"Input: '{s4}'")
print(f"Output: {result4} (Expected: 58)")

# Test Case 5: Complex number using multiple subtractive rules
s5 = "MCMXCIV"
# M (1000) + CM (900) + XC (90) + IV (4) = 1994
result5 = sol.romanToInt(s5)
print(f"Input: '{s5}'")
print(f"Output: {result5} (Expected: 1994)")

# Test Case 6: Maximum number
s6 = "MMMCMXCIX"
# 3999
result6 = sol.romanToInt(s6)
print(f"Input: '{s6}'")
print(f"Output: {result6} (Expected: 3999)")