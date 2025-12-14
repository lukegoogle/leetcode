class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        max_len = 0
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len

# --- Example Usage Code ---

sol = Solution()
print("--- Longest Valid Parentheses Examples ---")

# Test Case 1: Standard case
s1 = "(()"
result1 = sol.longestValidParentheses(s1)
# Expected: 2 (from "()")
print(f"Input: '{s1}'")
print(f"Output: {result1} (Expected: 2)")

# Test Case 2: Complex valid substring
s2 = ")()())"
result2 = sol.longestValidParentheses(s2)
# Expected: 4 (from "()()")
print(f"\nInput: '{s2}'")
print(f"Output: {result2} (Expected: 4)")

# Test Case 3: Fully valid
s3 = "()(())"
result3 = sol.longestValidParentheses(s3)
# Expected: 6
print(f"\nInput: '{s3}'")
print(f"Output: {result3} (Expected: 6)")

# Test Case 4: Long string with multiple parts
s4 = ")(()())(()("
result4 = sol.longestValidParentheses(s4)
# Expected: 6 (from "()()()" at index 2)
print(f"\nInput: '{s4}'")
print(f"Output: {result4} (Expected: 6)")

# Test Case 5: Empty string
s5 = ""
result5 = sol.longestValidParentheses(s5)
# Expected: 0
print(f"\nInput: '{s5}'")
print(f"Output: {result5} (Expected: 0)")