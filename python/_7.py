class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer $x$.

        The reversal process extracts the last digit of $x$ using the modulo operator 
        and prepends it to the `reversed_x` by multiplying `reversed_x` by 10.
        

        **Overflow Handling:**
        The operation must respect the constraints of a 32-bit signed integer, 
        which ranges from $INT\_MIN = -2^{31}$ to $INT\_MAX = 2^{31} - 1$. 
        If the reversed integer overflows or underflows, the function must return 0.

        The check for overflow/underflow is performed *before* the final multiplication 
        and addition step (`reversed_x = reversed_x * 10 + digit`) to ensure 
        no temporary overflow occurs.

        The conditions for returning 0 are:
        * **Positive Overflow:** $reversed\_x > INT\_MAX // 10$ or 
          ($reversed\_x == INT\_MAX // 10$ and $digit > 7$)
        * **Negative Underflow:** $reversed\_x < INT\_MIN // 10$ or 
          ($reversed\_x == INT\_MIN // 10$ and $digit < -8$)

        Args:
            x: The 32-bit signed integer to reverse.

        Returns:
            The reversed integer. Returns 0 if the reversed integer overflows 
            or underflows the 32-bit signed integer range.

        Examples:
            >>> sol = Solution()
            >>> sol.reverse(123)
            321
            >>> sol.reverse(-123)
            -321
            >>> sol.reverse(120)
            21
            >>> sol.reverse(1534236469) # Example of overflow
            0
        """
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        reversed_x = 0
        
        while x != 0:
            digit = x % 10
            # Special handling for Python's modulo operator with negative numbers
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            # Overflow check (before multiplication)
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0
            
            # Underflow check (before multiplication)
            if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
                return 0
            
            reversed_x = reversed_x * 10 + digit
            
        return reversed_x