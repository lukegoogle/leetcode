def myAtoi(s: str) -> int:
    i = 0
    n = len(s)
    
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    while i < n and s[i] == ' ':
        i += 1
        
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1
        
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        
        # Check against the positive limit (abs value check)
        if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
            return MAX_INT if sign == 1 else MIN_INT
            
        result = result * 10 + digit
        i += 1
        
    return sign * result