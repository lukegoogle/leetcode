class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        result = []
        
        def backtrack(remainder, combination, start):
            if remainder == 0:
                result.append(list(combination))
                return
            if remainder < 0:
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                candidate = candidates[i]
                combination.append(candidate)
                backtrack(remainder - candidate, combination, i + 1)
                combination.pop()
                
        backtrack(target, [], 0)
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- Combination Sum II Examples ---")

# Test Case 1: Duplicates in candidates
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
result1 = sol.combinationSum2(candidates1, target1)
# After sorting: [1, 1, 2, 5, 6, 7, 10]
# Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(f"Input: candidates={candidates1}, target={target1}")
print(f"Output: {result1}")

# Test Case 2: Duplicates in candidates (Simple case)
candidates2 = [2, 5, 2, 1, 2]
target2 = 5
result2 = sol.combinationSum2(candidates2, target2)
# After sorting: [1, 2, 2, 2, 5]
# Expected: [[1, 2, 2], [5]]
print(f"\nInput: candidates={candidates2}, target={target2}")
print(f"Output: {result2}")

# Test Case 3: No combination found
candidates3 = [3, 4]
target3 = 2
result3 = sol.combinationSum2(candidates3, target3)
# Expected: []
print(f"\nInput: candidates={candidates3}, target={target3}")
print(f"Output: {result3}")