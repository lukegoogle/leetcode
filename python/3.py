def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    l = 0
    max_len = 0
    
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_len = max(max_len, r - l + 1)
        
    return max_len

# Example Output
print("--- LeetCode 3 ---")
print(f"Output for 'abcabcbb': {lengthOfLongestSubstring('abcabcbb')}")
print(f"Output for 'bbbbb': {lengthOfLongestSubstring('bbbbb')}")