class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an integer $x$ is a palindrome.

        An integer is a palindrome when it reads the same backward as forward.
        This method converts only the *second half* of the number to its reverse
        and then compares it with the *first half* of the original number. This
        avoids potential integer overflow issues that could arise from reversing
        the entire number.

        The core logic involves three checks:
        1. **Edge Cases:** Returns `False` immediately if $x$ is negative or if $x$
           ends in 0 (since a number ending in 0 can only be a palindrome if it's 0 itself).
        2. **Reversing Half:** A loop iteratively builds `reverted_number` by
           taking digits from $x$ until `reverted_number` is greater than or equal to $x$.
           
        3. **Comparison:**
           * If the number has an **even** number of digits (e.g., 1221), the 
             loop terminates when $x$ and `reverted_number` are equal, and we 
             return `x == reverted_number`.
           * If the number has an **odd** number of digits (e.g., 121), the 
             middle digit will be in `reverted_number`. We remove the middle digit 
             from `reverted_number` by dividing it by 10, and then compare $x$ 
             with `reverted_number // 10`. We return `x == reverted_number // 10`.

        Args:
            x: The integer to check.

        Returns:
            True if $x$ is a palindrome, False otherwise.

        Examples:
            >>> sol = Solution()
            >>> sol.isPalindrome(121)
            True
            >>> sol.isPalindrome(-121)
            False
            >>> sol.isPalindrome(10)
            False
            >>> sol.isPalindrome(123454321)
            True
        """
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is even, x == reverted_number (e.g., 1221)
        # When the length is odd, x == reverted_number // 10 (e.g., 121, x=1, reverted_number=12)
        return x == reverted_number or x == reverted_number // 10