class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1

        def expand(l, r):
            nonlocal start, max_len
            
            while l >= 0 and r < n and s[l] == s[r]:
                current_len = r - l + 1
                if current_len > max_len:
                    max_len = current_len
                    start = l
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        
        return s[start:start + max_len]
    
solver = Solution()

# Test Case 1: babad -> bab
s1 = "babad"
result1 = solver.longestPalindrome(s1)
print(f"Input: \"{s1}\"")
print(f"Output: \"{result1}\"")

# Test Case 2: cbbd -> bb
s2 = "cbbd"
result2 = solver.longestPalindrome(s2)
print(f"Input: \"{s2}\"")
print(f"Output: \"{result2}\"")

# Test Case 3: racecar -> racecar
s3 = "racecar"
result3 = solver.longestPalindrome(s3)
print(f"Input: \"{s3}\"")
print(f"Output: \"{result3}\"")