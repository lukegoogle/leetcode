class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) != (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        for i in range(31, -1, -1):
            if (abs_dividend >> i) >= abs_divisor:
                quotient += (1 << i)
                abs_dividend -= (abs_divisor << i)
                
        if negative:
            return -quotient
        else:
            return quotient
        
# --- Example Usage Code ---

sol = Solution()
print("--- Divide Two Integers Examples ---")

# Test Case 1: Standard positive division
dividend1, divisor1 = 10, 3
result1 = sol.divide(dividend1, divisor1)
print(f"Input: {dividend1} / {divisor1}")
print(f"Output: {result1} (Expected: 3)")

# Test Case 2: Negative result
dividend2, divisor2 = 7, -3
result2 = sol.divide(dividend2, divisor2)
print(f"Input: {dividend2} / {divisor2}")
print(f"Output: {result2} (Expected: -2)")

# Test Case 3: Overflow edge case (MAX_INT)
dividend3, divisor3 = -2147483648, -1
result3 = sol.divide(dividend3, divisor3)
print(f"Input: {dividend3} / {divisor3}")
print(f"Output: {result3} (Expected: 2147483647)")

# Test Case 4: Dividend is smaller than divisor
dividend4, divisor4 = 1, 2
result4 = sol.divide(dividend4, divisor4)
print(f"Input: {dividend4} / {divisor4}")
print(f"Output: {result4} (Expected: 0)")

# Test Case 5: Large division
dividend5, divisor5 = 100, 10
result5 = sol.divide(dividend5, divisor5)
print(f"Input: {dividend5} / {divisor5}")
print(f"Output: {result5} (Expected: 10)")