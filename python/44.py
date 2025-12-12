def isMatch(s: str, p: str) -> bool:
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        if i == len(s):
            return p[j:] == '*' * len(p[j:])

        if p[j] == '?':
            result = dp(i + 1, j + 1)
        elif p[j] == '*':
            result = dp(i, j + 1) or dp(i + 1, j)
        elif s[i] == p[j]:
            result = dp(i + 1, j + 1)
        else:
            result = False
        
        memo[(i, j)] = result
        return result

    return dp(0, 0)

# Example Output
print(f"Output for ('aa', 'a'): {isMatch('aa', 'a')}")
print(f"Output for ('aa', '*'): {isMatch('aa', '*')}")
print(f"Output for ('adceb', 'a*b'): {isMatch('adceb', 'a*b')}")