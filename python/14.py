def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    lcp = strs[0]

    for i in range(1, len(strs)):
        while strs[i].find(lcp) != 0:
            lcp = lcp[:-1]
            if not lcp:
                return ""
    
    return lcp