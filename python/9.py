def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
        
    reversed_number = 0
    original = x
    
    while x > reversed_number:
        reversed_number = reversed_number * 10 + x % 10
        x //= 10
        
    return x == reversed_number or x == reversed_number // 10

# Example Output
print("--- LeetCode 9 ---")
print(f"Output for 121: {isPalindrome(121)}")
print(f"Output for -121: {isPalindrome(-121)}")
print(f"Output for 10: {isPalindrome(10)}")