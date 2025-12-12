def romanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        current_value = roman_map[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
            
        prev_value = current_value
        
    return total

# Example Output
print("--- LeetCode 13 ---")
print(f"Output for 'III': {romanToInt('III')}")
print(f"Output for 'LVIII': {romanToInt('LVIII')}")
print(f"Output for 'MCMXCIV': {romanToInt('MCMXCIV')}")