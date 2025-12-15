class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        if m > n:
            A, B = B, A
            m, n = n, m

        half_len = (m + n + 1) // 2
        
        low = 0
        high = m

        while low <= high:
            partitionA = (low + high) // 2
            partitionB = half_len - partitionA

            maxLeftA = A[partitionA - 1] if partitionA > 0 else float('-inf')
            minRightA = A[partitionA] if partitionA < m else float('inf')
            
            maxLeftB = B[partitionB - 1] if partitionB > 0 else float('-inf')
            minRightB = B[partitionB] if partitionB < n else float('inf')

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 1:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            
            elif maxLeftA > minRightB:
                high = partitionA - 1
            
            else:
                low = partitionA + 1
        
        return 0.0