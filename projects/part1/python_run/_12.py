class Solution:
    def intToRoman(self, num: int) -> str:
        
        mappings = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
            (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in mappings:
            if num == 0:
                break
            
            count, num = divmod(num, value)
            
            result.append(symbol * count)
            
        return "".join(result)
    
# --- Example Usage Code ---

sol = Solution()
print("--- Integer to Roman Examples ---")

# Test Case 1: Simple addition
num1 = 3
result1 = sol.intToRoman(num1)
print(f"Input: {num1}")
print(f"Output: '{result1}' (Expected: 'III')")

# Test Case 2: Subtractive notation (IV)
num2 = 4
result2 = sol.intToRoman(num2)
print(f"Input: {num2}")
print(f"Output: '{result2}' (Expected: 'IV')")

# Test Case 3: Mixed addition and subtraction
num3 = 58
# 50 (L) + 5 (V) + 3 (III)
result3 = sol.intToRoman(num3)
print(f"Input: {num3}")
print(f"Output: '{result3}' (Expected: 'LVIII')")

# Test Case 4: Complex number using multiple subtractive rules
num4 = 1994
# 1000 (M) + 900 (CM) + 90 (XC) + 4 (IV)
result4 = sol.intToRoman(num4)
print(f"Input: {num4}")
print(f"Output: '{result4}' (Expected: 'MCMXCIV')")

# Test Case 5: Maximum allowed input (3999)
num5 = 3999
# 3000 (MMM) + 900 (CM) + 90 (XC) + 9 (IX)
result5 = sol.intToRoman(num5)
print(f"Input: {num5}")
print(f"Output: '{result5}' (Expected: 'MMMCMXCIX')")