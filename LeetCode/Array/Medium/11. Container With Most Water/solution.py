# Complexity:
# Time: O(n), where n is the number of elements in the input list. We use a two-pointer approach that traverses the list at most once.
# Space: O(1), since we are using only a constant amount of extra space for the pointers and temporary variables.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area