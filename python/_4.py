class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays $nums1$ and $nums2$.

        This method merges the problem of finding the median into a search problem 
        by using binary search to find the correct partition point in the smaller array.
        The goal is to partition both arrays, $A$ and $B$, such that:
        1. The total number of elements in the left partition is $\lfloor (m+n+1)/2 \rfloor$.
        2. $\max(Left\_A) \le \min(Right\_B)$ and $\max(Left\_B) \le \min(Right\_A)$.
        
        

        The median is then calculated based on whether the total length is odd or even:
        - **Odd length:** $\max(\max(Left\_A), \max(Left\_B))$
        - **Even length:** $(\max(\max(Left\_A), \max(Left\_B)) + \min(\min(Right\_A), \min(Right\_B))) / 2$

        The time complexity is $O(\log(\min(m, n)))$ because the binary search is 
        performed on the smaller array.

        Args:
            nums1: The first sorted list of integers.
            nums2: The second sorted list of integers.

        Returns:
            The median of the two sorted arrays as a float.

        Examples:
            >>> sol = Solution()
            >>> sol.findMedianSortedArrays([1, 3], [2])
            2.0
            >>> sol.findMedianSortedArrays([1, 2], [3, 4])
            2.5
            >>> sol.findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])
            11.0
        """
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