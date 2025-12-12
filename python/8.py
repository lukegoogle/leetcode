def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
        
    sign = 1
    i = 0
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    result = 0
    
    if s[0] == '+':
        i = 1
    elif s[0] == '-':
        sign = -1
        i = 1
        
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        
        if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
            return MAX_INT if sign == 1 else MIN_INT
            
        result = result * 10 + digit
        i += 1
        
    return result * sign

# Example Output
print("--- LeetCode 8 ---")
print(f"Output for '42': {myAtoi('42')}")
print(f"Output for '   -42': {myAtoi('   -42')}")
print(f"Output for '4193 with words': {myAtoi('4193 with words')}")