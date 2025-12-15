class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[0] == '+':
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1
            
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            if sign == 1:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            else:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 8):
                    return INT_MIN
                    
            result = result * 10 + digit
            i += 1
            
        return result * sign
    
# --- Example Usage Code ---

sol = Solution()
print("--- String to Integer (atoi) Examples ---")

# Test Case 1: Standard positive conversion
s1 = "42"
result1 = sol.myAtoi(s1)
print(f"Input: '{s1}'")
print(f"Output: {result1} (Expected: 42)")

# Test Case 2: Conversion with leading whitespace and sign
s2 = "   -42"
result2 = sol.myAtoi(s2)
print(f"Input: '{s2}'")
print(f"Output: {result2} (Expected: -42)")

# Test Case 3: Conversion with non-digit characters after the number
s3 = "4193 with words"
result3 = sol.myAtoi(s3)
print(f"Input: '{s3}'")
print(f"Output: {result3} (Expected: 4193)")

# Test Case 4: No valid number found
s4 = "words and 987"
result4 = sol.myAtoi(s4)
print(f"Input: '{s4}'")
print(f"Output: {result4} (Expected: 0)")

# Test Case 5: Positive Overflow (Should return INT_MAX: 2147483647)
s5 = "91283472332"
result5 = sol.myAtoi(s5)
print(f"Input: '{s5}'")
print(f"Output: {result5} (Expected: 2147483647)")

# Test Case 6: Negative Overflow (Should return INT_MIN: -2147483648)
s6 = "-91283472332"
result6 = sol.myAtoi(s6)
print(f"Input: '{s6}'")
print(f"Output: {result6} (Expected: -2147483648)")

# Test Case 7: Only sign
s7 = "+"
result7 = sol.myAtoi(s7)
print(f"Input: '{s7}'")
print(f"Output: {result7} (Expected: 0)")

# Test Case 8: Exact positive boundary
s8 = "2147483647"
result8 = sol.myAtoi(s8)
print(f"Input: '{s8}'")
print(f"Output: {result8} (Expected: 2147483647)")

# Test Case 9: Exact negative boundary
s9 = "-2147483648"
result9 = sol.myAtoi(s9)
print(f"Input: '{s9}'")
print(f"Output: {result9} (Expected: -2147483648)")