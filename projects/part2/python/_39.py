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
