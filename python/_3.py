class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        This function uses a sliding window approach with a set to keep track of 
        characters within the current window $s[left:right+1]$.

        The algorithm works as follows:
        1. Initialize `char_set` (a set for the current window's characters), 
           `left` (the start of the window), and `max_length` (the longest 
           found length).
        2. Iterate through the string with `right` (the end of the window).
        3. **Sliding:** If the character $s[right]$ is already in `char_set`, 
           it means we have a duplicate. We shrink the window from the `left` 
           by removing $s[left]$ from `char_set` and incrementing `left` until 
           the duplicate character $s[right]$ is removed from the window 
           (i.e., $s[right]$ is no longer in `char_set`).
        4. **Expansion:** Add $s[right]$ to `char_set` to expand the window.
        5. **Update Max:** Calculate the current window length (`right - left + 1`) 
           and update `max_length` if the current length is greater.
        6. Return `max_length` after iterating through the entire string.

        

        :param s: The input string.
        :type s: str
        :raises TypeError: If the input `s` is not a string.
        :return: The length of the longest substring without repeating characters.
        :rtype: int
        
        Example:
        >>> sol = Solution()
        >>> sol.lengthOfLongestSubstring("abcabcbb")
        3  # The longest substring is "abc"
        >>> sol.lengthOfLongestSubstring("bbbbb")
        1  # The longest substring is "b"
        >>> sol.lengthOfLongestSubstring("pwwkew")
        3  # The longest substring is "wke". Note that "pwke" is a subsequence, not a substring.
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            
        return max_length