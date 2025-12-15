class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
    
# --- Example Usage Code ---

sol = Solution()
print("--- Regular Expression Matching Examples ---")
# 

# Test Case 1: Simple mismatch
s1 = "aa"
p1 = "a"
result1 = sol.isMatch(s1, p1)
print(f"Input: s='{s1}', p='{p1}'")
print(f"Output: {result1} (Expected: False)")

# Test Case 2: Simple * match (one or more 'a')
s2 = "aa"
p2 = "a*"
result2 = sol.isMatch(s2, p2)
print(f"Input: s='{s2}', p='{p2}'")
print(f"Output: {result2} (Expected: True)")

# Test Case 3: Zero * match (zero 'a')
s3 = "ab"
p3 = ".*"
result3 = sol.isMatch(s3, p3)
print(f"Input: s='{s3}', p='{p3}'")
print(f"Output: {result3} (Expected: True)")

# Test Case 4: Multiple characters and *
s4 = "aab"
p4 = "c*a*b"
result4 = sol.isMatch(s4, p4)
print(f"Input: s='{s4}', p='{p4}'")
print(f"Output: {result4} (Expected: True) (c* matches zero c's, a* matches two a's)")

# Test Case 5: Complex match with '.' and '*'
s5 = "mississippi"
p5 = "mis*is*p*."
result5 = sol.isMatch(s5, p5)
print(f"Input: s='{s5}', p='{p5}'")
print(f"Output: {result5} (Expected: False)")

# Test Case 6: Edge Case (Pattern starts with '.*')
s6 = "abcd"
p6 = ".*d"
result6 = sol.isMatch(s6, p6)
print(f"Input: s='{s6}', p='{p6}'")
print(f"Output: {result6} (Expected: True)")