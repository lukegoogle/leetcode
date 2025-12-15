class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def find_bound(is_first):
            L, R = 0, len(nums) - 1
            idx = -1
            
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] == target:
                    idx = mid
                    if is_first:
                        R = mid - 1
                    else:
                        L = mid + 1
                elif nums[mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
            return idx
            
        first = find_bound(True)
        if first == -1:
            return [-1, -1]
            
        last = find_bound(False)
        return [first, last]
    