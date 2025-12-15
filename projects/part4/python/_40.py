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
    