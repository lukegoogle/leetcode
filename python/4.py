def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2
    m, n = len(A), len(B)
    
    if m > n:
        A, B, m, n = B, A, n, m

    total = m + n
    half = (total + 1) // 2
    
    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2
        j = half - i
        
        L1 = A[i - 1] if i > 0 else float('-inf')
        R1 = A[i] if i < m else float('inf')

        L2 = B[j - 1] if j > 0 else float('-inf')
        R2 = B[j] if j < n else float('inf')
        
        if L1 <= R2 and L2 <= R1:
            if total % 2 == 1:
                return max(L1, L2)
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
                
        elif L1 > R2:
            high = i - 1
            
        else:
            low = i + 1
            
    return 0.0