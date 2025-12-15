class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            L = i + 1
            R = n - 1
            
            while L < R:
                current_sum = nums[L] + nums[R]
                
                if current_sum == target:
                    result.append([nums[i], nums[L], nums[R]])
                    
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                        
                    L += 1
                    R -= 1
                    
                elif current_sum < target:
                    L += 1
                    
                else:
                    R -= 1
                    
        return result
