class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        
        if not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        from collections import Counter
        word_count = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        
                    if right - left == total_len:
                        result.append(left)
                else:
                    current_count.clear()
                    left = right
                    
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- Substring with Concatenation of All Words Examples ---")

# Test Case 1: Standard example
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
result1 = sol.findSubstring(s1, words1)
# Expected: [0, 9] ("barfoo" at 0, "foobar" at 9)
print(f"Input: s='{s1}', words={words1}")
print(f"Output: {result1} (Expected: [0, 9])")

# Test Case 2: Overlapping words, multiple results
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
result2 = sol.findSubstring(s2, words2)
# Expected: [] (The three 'good's are not covered by the required words)
print(f"\nInput: s='{s2}', words={words2}")
print(f"Output: {result2} (Expected: [])")

# Test Case 3: Duplicates in words
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
result3 = sol.findSubstring(s3, words3)
# Expected: [6, 9, 12]
print(f"\nInput: s='{s3}', words={words3}")
print(f"Output: {result3} (Expected: [6, 9, 12])")

# Test Case 4: Long string with words that are not found
s4 = "barfoobarman"
words4 = ["man", "bar"]
result4 = sol.findSubstring(s4, words4)
# Expected: [6] ("manbar" is not present, but "barman" is not valid. The only valid is "foobarman" where "bar" is at 6)
# Correct Expected: [6] ("barfoobarman" -> "bar" at 0, "foo" at 3, "bar" at 6, "man" at 9. Valid concatenation is "barfoo" or "foobar", but target is 2 words.
# "foobar" at 6: "barman" - No.
# "barfoobarman" - word_len=3, num_words=2, total_len=6
# Window 0-5: "barfoo". Words: ["bar", "foo"]. Match. Index 0.
# Window 3-8: "foothe". Words: ["foo", "the"]. Target: ["man", "bar"]. No match.
# Correct Expected: [6] for ["bar", "foo", "the"] is wrong.
# Correct for words4: ["man", "bar"] is target.
# Index 6: "barman" -> ["bar", "man"]. Match. Index 6.
print(f"\nInput: s='{s4}', words={words4}")
print(f"Output: {result4} (Expected: [6])")