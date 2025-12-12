def longestPalindrome(s: str) -> str:
    res = ""
    res_len = 0
    
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
            
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
            
    return res

# Example Output
print("--- LeetCode 5 ---")
print(f"Output for 'babad': {longestPalindrome('babad')}")
print(f"Output for 'cbbd': {longestPalindrome('cbbd')}")