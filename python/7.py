def reverse(x: int) -> int:
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    reversed_num = 0
    
    temp = abs(x)

    while temp != 0:
        digit = temp % 10
        temp //= 10
        
        # Positive overflow check
        if reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 7):
            return 0
        
        # Negative overflow check (magnitude check)
        # -2**31 is -2147483648 (last digit 8)
        if x < 0 and (reversed_num > MAX_INT // 10 or (reversed_num == MAX_INT // 10 and digit > 8)):
             return 0

        reversed_num = reversed_num * 10 + digit
        
    return reversed_num if x >= 0 else -reversed_num