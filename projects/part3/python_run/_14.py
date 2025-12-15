class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            while current_string.find(prefix) != 0:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
                    
        return prefix
    
# --- Example Usage Code ---

sol = Solution()
print("--- Longest Common Prefix Examples ---")

# Test Case 1: Standard common prefix
strs1 = ["flower", "flow", "flight"]
result1 = sol.longestCommonPrefix(strs1)
print(f"Input: {strs1}")
print(f"Output: '{result1}' (Expected: 'fl')")

# Test Case 2: No common prefix
strs2 = ["dog", "racecar", "car"]
result2 = sol.longestCommonPrefix(strs2)
print(f"Input: {strs2}")
print(f"Output: '{result2}' (Expected: '')")

# Test Case 3: Common prefix is the full word
strs3 = ["apple", "app", "apricot"]
result3 = sol.longestCommonPrefix(strs3)
print(f"Input: {strs3}")
print(f"Output: '{result3}' (Expected: 'ap')")

# Test Case 4: Empty input list
strs4 = []
result4 = sol.longestCommonPrefix(strs4)
print(f"Input: {strs4}")
print(f"Output: '{result4}' (Expected: '')")

# Test Case 5: List with one string
strs5 = ["solo"]
result5 = sol.longestCommonPrefix(strs5)
print(f"Input: {strs5}")
print(f"Output: '{result5}' (Expected: 'solo')")

# Test Case 6: Vertically aligned mismatch
strs6 = ["ab", "a"]
result6 = sol.longestCommonPrefix(strs6)
print(f"Input: {strs6}")
print(f"Output: '{result6}' (Expected: 'a')")