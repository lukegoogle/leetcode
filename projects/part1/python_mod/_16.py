class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            L = i + 1
            R = n - 1
            
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    L += 1
                elif current_sum > target:
                    R -= 1
                else:
                    return current_sum
                    
        return closest_sum
