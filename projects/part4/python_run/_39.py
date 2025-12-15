class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []
        
        def backtrack(remainder, combination, start):
            if remainder == 0:
                result.append(list(combination))
                return
            if remainder < 0:
                return
                
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)
                backtrack(remainder - candidate, combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return result
    
# --- Example Usage Code ---

sol = Solution()
print("--- Combination Sum Examples ---")

# Test Case 1: Standard case with reuse
candidates1 = [2, 3, 6, 7]
target1 = 7
result1 = sol.combinationSum(candidates1, target1)
# Expected: [[2, 2, 3], [7]]
print(f"Input: candidates={candidates1}, target={target1}")
print(f"Output: {result1}")

# Test Case 2: Different candidates, multiple solutions
candidates2 = [2, 3, 5]
target2 = 8
result2 = sol.combinationSum(candidates2, target2)
# Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(f"\nInput: candidates={candidates2}, target={target2}")
print(f"Output: {result2}")

# Test Case 3: Target unreachable
candidates3 = [2, 4]
target3 = 7
result3 = sol.combinationSum(candidates3, target3)
# Expected: []
print(f"\nInput: candidates={candidates3}, target={target3}")
print(f"Output: {result3}")

# Test Case 4: Single candidate
candidates4 = [1]
target4 = 5
result4 = sol.combinationSum(candidates4, target4)
# Expected: [[1, 1, 1, 1, 1]]
print(f"\nInput: candidates={candidates4}, target={target4}")
print(f"Output: {result4}")