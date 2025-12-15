class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                new_target = target - nums[i] - nums[j]
                L = j + 1
                R = n - 1
                
                while L < R:
                    current_sum = nums[L] + nums[R]
                    
                    if current_sum == new_target:
                        result.append([nums[i], nums[j], nums[L], nums[R]])
                        
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                            
                        L += 1
                        R -= 1
                        
                    elif current_sum < new_target:
                        L += 1
                    else:
                        R -= 1
                        
        return result
    