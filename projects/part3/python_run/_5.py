class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            
            # Odd length palindromes (center is s[i])
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            # Even length palindromes (center is s[i] and s[i+1])
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
                
        return longest

# --- Output Examples Code ---

print("--- Longest Palindromic Substring Examples ---")

# Create an instance of the Solution class
sol = Solution()

# Test Case 1: Odd length palindrome (bab or aba)
s1 = "babad"
result1 = sol.longestPalindrome(s1)
print(f"Input: '{s1}'")
print(f"Output: '{result1}' (Expected: 'bab' or 'aba')") 

# Test Case 2: Even length palindrome
s2 = "cbbd"
result2 = sol.longestPalindrome(s2)
print(f"Input: '{s2}'")
print(f"Output: '{result2}' (Expected: 'bb')")

# Test Case 3: Whole string is a palindrome
s3 = "racecar"
result3 = sol.longestPalindrome(s3)
print(f"Input: '{s3}'")
print(f"Output: '{result3}' (Expected: 'racecar')")

# Test Case 4: Long even length palindrome in the middle
s4 = "forgeeksskeegfor"
result4 = sol.longestPalindrome(s4)
print(f"Input: '{s4}'")
print(f"Output: '{result4}' (Expected: 'geeksskeeg')")

# Test Case 5: Single character string
s5 = "x"
result5 = sol.longestPalindrome(s5)
print(f"Input: '{s5}'")
print(f"Output: '{result5}' (Expected: 'x')")

# Test Case 6: Empty string
s6 = ""
result6 = sol.longestPalindrome(s6)
print(f"Input: '{s6}'")
print(f"Output: '{result6}' (Expected: '')")