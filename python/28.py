def strStr(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)

    if m == 0:
        return 0

    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i

    return -1

# Example Output
print(f"Output for ('sadbutsad', 'sad'): {strStr('sadbutsad', 'sad')}")
print(f"Output for ('leetcode', 'leeto'): {strStr('leetcode', 'leeto')}")
print(f"Output for ('hello', ''): {strStr('hello', '')}")