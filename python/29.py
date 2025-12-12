def divide(dividend: int, divisor: int) -> int:
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    negative = (dividend < 0) != (divisor < 0)
    
    a = abs(dividend)
    b = abs(divisor)
    
    quotient = 0
    
    while a >= b:
        temp = b
        multiple = 1
        while a >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        a -= temp
        quotient += multiple
        
    if negative:
        return -quotient
    else:
        return quotient

# Example Output
print(f"Output for (10, 3): {divide(10, 3)}")
print(f"Output for (7, -3): {divide(7, -3)}")
print(f"Output for (2147483647, 1): {divide(2147483647, 1)}")
print(f"Output for (-2147483648, -1): {divide(-2147483648, -1)}")