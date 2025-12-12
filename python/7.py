def reverse(x: int) -> int:
    MIN_INT = -2**31
    MAX_INT = 2**31 - 1
    
    sign = -1 if x < 0 else 1
    abs_x = abs(x)
    reversed_x = 0
    
    while abs_x != 0:
        digit = abs_x % 10
        
        if reversed_x > MAX_INT // 10 or (reversed_x == MAX_INT // 10 and digit > 7):
            return 0
            
        reversed_x = reversed_x * 10 + digit
        abs_x //= 10
        
    final_result = reversed_x * sign
    
    if final_result < MIN_INT or final_result > MAX_INT:
        return 0
        
    return final_result

# Example Output
print("--- LeetCode 7 ---")
print(f"Output for 123: {reverse(123)}")
print(f"Output for -123: {reverse(-123)}")
print(f"Output for 120: {reverse(120)}")