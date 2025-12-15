class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
                
        return -1
    
# --- Example Usage Code ---

sol = Solution()
print("--- Find the Index of the First Occurrence in a String Examples ---")

# Test Case 1: Standard match
haystack1 = "sadbutsad"
needle1 = "sad"
result1 = sol.strStr(haystack1, needle1)
print(f"Haystack: '{haystack1}', Needle: '{needle1}'")
print(f"Output: {result1} (Expected: 0)")

# Test Case 2: No match
haystack2 = "leetcode"
needle2 = "leeto"
result2 = sol.strStr(haystack2, needle2)
print(f"\nHaystack: '{haystack2}', Needle: '{needle2}'")
print(f"Output: {result2} (Expected: -1)")

# Test Case 3: Empty needle
haystack3 = "abc"
needle3 = ""
result3 = sol.strStr(haystack3, needle3)
print(f"\nHaystack: '{haystack3}', Needle: '{needle3}'")
print(f"Output: {result3} (Expected: 0)")

# Test Case 4: Match in the middle
haystack4 = "hello"
needle4 = "ll"
result4 = sol.strStr(haystack4, needle4)
print(f"\nHaystack: '{haystack4}', Needle: '{needle4}'")
print(f"Output: {result4} (Expected: 2)")

# Test Case 5: Match at the end
haystack5 = "mississippi"
needle5 = "pi"
result5 = sol.strStr(haystack5, needle5)
print(f"\nHaystack: '{haystack5}', Needle: '{needle5}'")
print(f"Output: {result5} (Expected: 9)")