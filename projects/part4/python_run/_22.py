class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        result = []
        
        def backtrack(open_count, close_count, current_string):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
                
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")
                
        backtrack(0, 0, "")
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- Generate Parentheses Examples ---")

# Test Case 1: n = 3
n1 = 3
result1 = sol.generateParenthesis(n1)
# Expected: ["((()))","(()())","(())()","()(())","()()()"]
print(f"Input: n={n1}")
print(f"Output: {result1}")
print(f"Count: {len(result1)} (Expected: 5)")

# Test Case 2: n = 1
n2 = 1
result2 = sol.generateParenthesis(n2)
# Expected: ["()"]
print(f"Input: n={n2}")
print(f"Output: {result2}")
print(f"Count: {len(result2)} (Expected: 1)")

# Test Case 3: n = 2
n3 = 2
result3 = sol.generateParenthesis(n3)
# Expected: ["(())", "()()"]
print(f"Input: n={n3}")
print(f"Output: {result3}")
print(f"Count: {len(result3)} (Expected: 2)")