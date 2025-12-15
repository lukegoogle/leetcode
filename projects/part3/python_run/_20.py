class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack
    
# --- Example Usage Code ---

sol = Solution()
print("--- Valid Parentheses Examples ---")

# Test Case 1: Valid string
s1 = "()[]{}"
result1 = sol.isValid(s1)
print(f"Input: '{s1}'")
print(f"Output: {result1} (Expected: True)")

# Test Case 2: Invalid order
s2 = "(]"
result2 = sol.isValid(s2)
print(f"Input: '{s2}'")
print(f"Output: {result2} (Expected: False)")

# Test Case 3: Invalid closing type
s3 = "([)]"
result3 = sol.isValid(s3)
print(f"Input: '{s3}'")
print(f"Output: {result3} (Expected: False)")

# Test Case 4: Valid nested string
s4 = "{[]}"
result4 = sol.isValid(s4)
print(f"Input: '{s4}'")
print(f"Output: {result4} (Expected: True)")

# Test Case 5: Unclosed bracket (stack not empty at end)
s5 = "([{"
result5 = sol.isValid(s5)
print(f"Input: '{s5}'")
print(f"Output: {result5} (Expected: False)")

# Test Case 6: Closed bracket with empty stack (placeholder mismatch)
s6 = ")))"
result6 = sol.isValid(s6)
print(f"Input: '{s6}'")
print(f"Output: {result6} (Expected: False)")