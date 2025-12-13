class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        if m > n:
            A, B = B, A
            m, n = n, m
        
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            L1 = A[i-1] if i > 0 else float('-inf')
            R1 = A[i] if i < m else float('inf')
            L2 = B[j-1] if j > 0 else float('-inf')
            R2 = B[j] if j < n else float('inf')

            if L1 <= R2 and L2 <= R1:
                
                if (m + n) % 2 == 1:
                    return max(L1, L2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            
            elif L1 > R2:
                high = i - 1
            
            else:
                low = i + 1
        
        return 0.0

solver = Solution()

# Test Case 1: [1, 2] and [3, 4]. Merged: [1, 2, 3, 4]. Median: 2.5
nums1_1 = [1, 2]
nums1_2 = [3, 4]
result1 = solver.findMedianSortedArrays(nums1_1, nums1_2)
print(f"Input 1: {nums1_1}, {nums1_2}")
print(f"Output: {result1}")

# Test Case 2: [1, 3] and [2]. Merged: [1, 2, 3]. Median: 2.0
nums2_1 = [1, 3]
nums2_2 = [2]
result2 = solver.findMedianSortedArrays(nums2_1, nums2_2)
print(f"Input 2: {nums2_1}, {nums2_2}")
print(f"Output: {result2}")

# Test Case 3: [0, 0] and [0, 0]. Merged: [0, 0, 0, 0]. Median: 0.0
nums3_1 = [0, 0]
nums3_2 = [0, 0]
result3 = solver.findMedianSortedArrays(nums3_1, nums3_2)
print(f"Input 3: {nums3_1}, {nums3_2}")
print(f"Output: {result3}")