class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        reversed_x = 0
        
        while x != 0:
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0
            
            if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
                return 0
            
            reversed_x = reversed_x * 10 + digit
            
        return reversed_x

sol = Solution()
print("--- Reverse Integer Examples ---")
    
# Test Case 1: Positive number
x1 = 123
result1 = sol.reverse(x1)
print(f"Input: {x1}")
print(f"Output: {result1} (Expected: 321)")

# Test Case 2: Negative number
x2 = -123
result2 = sol.reverse(x2)
print(f"Input: {x2}")
print(f"Output: {result2} (Expected: -321)")

# Test Case 3: Number with trailing zeros
x3 = 120
result3 = sol.reverse(x3)
print(f"Input: {x3}")
print(f"Output: {result3} (Expected: 21)")

# Test Case 4: Positive Overflow Check (Max is 2147483647)
# Reversing 1534236469 gives 9646324351, which exceeds INT_MAX
x4 = 1534236469 
result4 = sol.reverse(x4)
print(f"Input: {x4}")
print(f"Output: {result4} (Expected: 0 - Overflow)")

# Test Case 5: Negative Overflow Check (Min is -2147483648)
# Reversing -1534236469 gives -9646324351, which is less than INT_MIN
x5 = -1534236469
result5 = sol.reverse(x5)
print(f"Input: {x5}")
print(f"Output: {result5} (Expected: 0 - Overflow)")
    
# Test Case 6: Exact INT_MAX reversal (No Overflow)
# Reversing 1463847412 (214748364 * 10 + 7) -> 2147483641
x6 = 1463847412 # Just a large number whose reverse is safe
result6 = sol.reverse(x6)
print(f"Input: {x6}")
print(f"Output: {result6} (Expected: 2147483641)")