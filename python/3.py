class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len
    
solver = Solution()

# Test Case 1: abcabcbb -> abc (length 3)
s1 = "abcabcbb"
result1 = solver.lengthOfLongestSubstring(s1)
print(f"Input: \"{s1}\"")
print(f"Output: {result1}")

# Test Case 2: bbbbb -> b (length 1)
s2 = "bbbbb"
result2 = solver.lengthOfLongestSubstring(s2)
print(f"Input: \"{s2}\"")
print(f"Output: {result2}")

# Test Case 3: pwwkew -> wke or kew (length 3)
s3 = "pwwkew"
result3 = solver.lengthOfLongestSubstring(s3)
print(f"Input: \"{s3}\"")
print(f"Output: {result3}")