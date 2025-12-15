class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        return x == reverted_number or x == reverted_number // 10
    
# --- Example Usage Code ---

sol = Solution()
print("--- Palindrome Number Examples ---")

# Test Case 1: Standard Palindrome (Odd number of digits)
x1 = 121
result1 = sol.isPalindrome(x1)
print(f"Input: {x1}")
print(f"Output: {result1} (Expected: True)")

# Test Case 2: Standard Palindrome (Even number of digits)
x2 = 1221
result2 = sol.isPalindrome(x2)
print(f"Input: {x2}")
print(f"Output: {result2} (Expected: True)")

# Test Case 3: Not a Palindrome
x3 = 10
result3 = sol.isPalindrome(x3)
print(f"Input: {x3}")
print(f"Output: {result3} (Expected: False - Fails condition 2)")

# Test Case 4: Not a Palindrome (Mismatch)
x4 = 123
result4 = sol.isPalindrome(x4)
print(f"Input: {x4}")
print(f"Output: {result4} (Expected: False)")

# Test Case 5: Negative Number (Fails condition 1)
x5 = -121
result5 = sol.isPalindrome(x5)
print(f"Input: {x5}")
print(f"Output: {result5} (Expected: False)")

# Test Case 6: Zero (Palindrome)
x6 = 0
result6 = sol.isPalindrome(x6)
print(f"Input: {x6}")
print(f"Output: {result6} (Expected: True)")