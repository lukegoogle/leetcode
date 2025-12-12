def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, current_combination):
        if index == len(digits):
            result.append("".join(current_combination))
            return
            
        digit = digits[index]
        letters = mapping[digit]
        
        for letter in letters:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()

    backtrack(0, [])
    return result

# Example Output
print("--- LeetCode 17 ---")
print(f"Output for '23': {letterCombinations('23')}")
print(f"Output for '2': {letterCombinations('2')}")