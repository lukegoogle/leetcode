def findSubstring(s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    result = []
    n = len(s)

    for i in range(n - total_len + 1):
        substring = s[i : i + total_len]
        seen = {}
        j = 0
        
        while j < total_len:
            word = substring[j : j + word_len]
            
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                
                if seen[word] > word_count[word]:
                    break
            else:
                break
                
            j += word_len
            
        if j == total_len:
            result.append(i)

    return result

# Example Output
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(f"Output for ('{s1}', {words1}): {findSubstring(s1, words1)}")

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(f"Output for ('{s2}', {words2}): {findSubstring(s2, words2)}")