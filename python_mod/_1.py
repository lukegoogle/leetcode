class Solution:
    """
    Solution class for LeetCode problem 1: Two Sum.

    The problem asks to find two indices of the numbers in a list that add up
    to a specific target. The provided solution implements an efficient
    O(n) approach using a hash map (dictionary) for quick lookups.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in the input list that add up to a specific target.

        This method uses a hash map (dictionary in Python) to store the numbers
        encountered so far and their indices. For each number, it calculates the
        'complement' (the number needed to reach the target) and checks if this
        complement is already in the hash map. If it is, the indices of the
        complement and the current number are returned. Otherwise, the current
        number and its index are added to the hash map.

        The time complexity is O(n) because the list is traversed only once,
        and hash map lookups are O(1) on average.

        Args:
            nums (list[int]): The list of integers to search within.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the indices of the two numbers that
                       add up to the target. Returns an empty list if no such
                       pair is found.

        Examples:
            >>> solution = Solution()
            >>> solution.twoSum([2, 7, 11, 15], 9)
            [0, 1]
            >>> solution.twoSum([3, 2, 4], 6)
            [1, 2]
            >>> solution.twoSum([3, 3], 6)
            [0, 1]
            >>> solution.twoSum([1, 2, 3, 4], 10)
            []
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []

print(Solution().twoSum([0,1,2,3,4,5],2))