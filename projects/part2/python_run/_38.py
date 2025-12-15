class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        prev_sequence = self.countAndSay(n - 1)
        result = []
        i = 0
        
        while i < len(prev_sequence):
            count = 1
            j = i + 1
            while j < len(prev_sequence) and prev_sequence[j] == prev_sequence[i]:
                count += 1
                j += 1
            result.append(str(count) + prev_sequence[i])
            i = j
            
        return "".join(result)
    
# --- Example Usage Code ---

sol = Solution()
print("--- Count and Say Sequence Examples ---")

# Test Case 1: n = 1
n1 = 1
result1 = sol.countAndSay(n1)
print(f"Input: n={n1}")
print(f"Output: '{result1}' (Expected: '1')")

# Test Case 2: n = 4
n2 = 4
result2 = sol.countAndSay(n2)
# n=1: 1
# n=2: 11
# n=3: 21
# n=4: 1211
print(f"\nInput: n={n2}")
print(f"Output: '{result2}' (Expected: '1211')")

# Test Case 3: n = 5
n3 = 5
result3 = sol.countAndSay(n3)
# n=5: 111221
print(f"\nInput: n={n3}")
print(f"Output: '{result3}' (Expected: '111221')")

# Test Case 4: n = 6
n4 = 6
result4 = sol.countAndSay(n4)
# n=6: 312211
print(f"\nInput: n={n4}")
print(f"Output: '{result4}' (Expected: '312211')")