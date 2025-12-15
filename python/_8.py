class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Implements the `atoi` function, which converts a string to a 32-bit signed integer.

        The algorithm follows specific rules for processing the input string:
        1. **Whitespace:** Discards any leading whitespace characters.
        2. **Sign:** Checks for an optional leading sign ('+' or '-'). If present, 
           it determines the sign of the result.
        3. **Digits:** Reads the subsequent characters until the first non-digit 
           character or the end of the string is reached.
        4. **Conversion:** Converts these digits into an integer.
        5. **Clamping:** If the resulting integer is out of the 32-bit signed 
           integer range [$-2^{31}$, $2^{31} - 1$], it is clamped.
           The range limits are:
           * $INT\_MAX = 2,147,483,647$
           * $INT\_MIN = -2,147,483,648$
        6. **Invalid Input:** If no valid conversion could be performed, 0 is returned.

        Special attention is paid to **overflow checking** within the loop 
        before multiplication to ensure the calculated `result` does not exceed 
        the $INT\_MAX$ or fall below $INT\_MIN$.

        Args:
            s: The input string.

        Returns:
            The converted 32-bit signed integer.

        Examples:
            >>> sol = Solution()
            >>> sol.myAtoi("42")
            42
            >>> sol.myAtoi("   -42")
            -42
            >>> sol.myAtoi("4193 with words")
            4193
            >>> sol.myAtoi("words and 987")
            0
            >>> sol.myAtoi("-91283472332")  # Example of clamping to INT_MIN
            -2147483648
        """
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[0] == '+':
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1
            
        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Overflow Check
            # For positive numbers: Check if (result * 10 + digit) > INT_MAX
            if sign == 1:
                # result > INT_MAX // 10: result * 10 will already overflow
                # (result == INT_MAX // 10 and digit > 7): result * 10 + digit will overflow (INT_MAX ends in 7)
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            # For negative numbers: Check if (result * 10 + digit) * -1 < INT_MIN
            # We check the absolute value, so we are checking if result * 10 + digit > |INT_MIN|
            else:
                # result > INT_MAX // 10: result * 10 will already overflow in magnitude
                # (result == INT_MAX // 10 and digit > 8): result * 10 + digit will exceed |INT_MIN| (INT_MIN magnitude ends in 8)
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 8):
                    return INT_MIN
                    
            result = result * 10 + digit
            i += 1
            
        return result * sign