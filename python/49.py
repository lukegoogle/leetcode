def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    
    for s in strs:
        key = tuple(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
        
    return list(anagrams.values())

# Example Output
print(f"Output for ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']: {groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])}")
print(f"Output for ['a']: {groupAnagrams(['a'])}")