class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the input string $s$.

        This method uses the "Expand Around Center" technique. It iterates through 
        every possible center of a palindrome and expands outwards to find the longest 
        palindromic substring centered there. 

        A center can be:
        1. A single character (for odd-length palindromes, e.g., "aba" centered at 'b').
           This corresponds to calling `expand_around_center(i, i)`.
        2. Two adjacent characters (for even-length palindromes, e.g., "abba" centered 
           between the two 'b's).
           This corresponds to calling `expand_around_center(i, i + 1)`.

        The overall algorithm checks $2N - 1$ possible centers (where $N$ is the length 
        of the string), ensuring all possible palindromes are considered.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring found in $s$. If multiple exist, 
            any of them can be returned.

        Examples:
            >>> sol = Solution()
            >>> sol.longestPalindrome("babad")
            'bab'  # or 'aba'
            >>> sol.longestPalindrome("cbbd")
            'bb'
            >>> sol.longestPalindrome("a")
            'a'
        """
        
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