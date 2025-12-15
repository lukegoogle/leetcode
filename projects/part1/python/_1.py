class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two unique numbers in the input list that sum up to a specific target 
        value and returns the 0-based indices of those two numbers. The function 
        uses a hash map to achieve a time complexity of $O(n)$ by storing each 
        number and its index as it iterates through the list, then checking if 
        the required complement (target - current number) already exists in the map.

        Args:
            nums: A list of integers where exactly one valid solution exists.
            target: The target integer sum.

        Returns:
            A list containing the indices of the two numbers that sum up to the target, 
            e.g., [index1, index2].
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []