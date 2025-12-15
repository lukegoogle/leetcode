class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) != (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        for i in range(31, -1, -1):
            if (abs_dividend >> i) >= abs_divisor:
                quotient += (1 << i)
                abs_dividend -= (abs_divisor << i)
                
        if negative:
            return -quotient
        else:
            return quotient
        