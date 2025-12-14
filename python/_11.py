class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
# --- Example Usage Code ---

sol = Solution()
print("--- Container With Most Water Examples ---")

# Test Case 1: Standard Example
# The maximum area is 49, formed by the lines of height 8 and 7, which are 7 units apart.
h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result1 = sol.maxArea(h1)
print(f"Input: {h1}")
print(f"Output: {result1} (Expected: 49)")

# Test Case 2: Simple Example
h2 = [1, 1]
result2 = sol.maxArea(h2)
print(f"Input: {h2}")
print(f"Output: {result2} (Expected: 1)")

# Test Case 3: Decreasing heights
# Max area is formed by the first and last line: min(5, 1) * 4 = 4
h3 = [5, 4, 3, 2, 1]
result3 = sol.maxArea(h3)
print(f"Input: {h3}")
print(f"Output: {result3} (Expected: 4)")

# Test Case 4: Increasing heights
# Max area is formed by the first and last line: min(1, 5) * 4 = 4
h4 = [1, 2, 3, 4, 5]
result4 = sol.maxArea(h4)
print(f"Input: {h4}")
print(f"Output: {result4} (Expected: 4)")

# Test Case 5: Large example with max area far from edges
h5 = [2, 3, 4, 5, 18, 17, 6]
# Max area is min(18, 17) * 1 = 17 OR min(5, 6) * 3 = 15. The true max is likely from 18 and 17.
result5 = sol.maxArea(h5)
print(f"Input: {h5}")
print(f"Output: {result5} (Expected: 17)")