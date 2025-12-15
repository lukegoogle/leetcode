class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if not digits:
            return []
            
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            
            digit = digits[index]
            letters = mapping[digit]
            
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- Letter Combinations of a Phone Number Examples ---")

# Test Case 1: Standard two-digit input
digits1 = "23"
result1 = sol.letterCombinations(digits1)
# Expected: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(f"Input: '{digits1}'")
print(f"Output: {result1}")
print(f"Count: {len(result1)} (Expected: 9)")

# Test Case 2: Empty input
digits2 = ""
result2 = sol.letterCombinations(digits2)
print(f"Input: '{digits2}'")
print(f"Output: {result2} (Expected: [])")

# Test Case 3: Single digit input (7 has 4 letters)
digits3 = "7"
result3 = sol.letterCombinations(digits3)
# Expected: ["p", "q", "r", "s"]
print(f"Input: '{digits3}'")
print(f"Output: {result3}")
print(f"Count: {len(result3)} (Expected: 4)")

# Test Case 4: Longer input (3 digits)
digits4 = "567"
result4 = sol.letterCombinations(digits4)
# Expected count: 3 * 3 * 4 = 36
print(f"Input: '{digits4}'")
print(f"Output: {result4[:5]}... (Showing first 5 combinations)")
print(f"Count: {len(result4)} (Expected: 36)")