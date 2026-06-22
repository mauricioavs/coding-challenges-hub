# Complexity:
# Time: O(log n): In each iteration, we are halving the search space, resulting in logarithmic time complexity.
# Space: O(1): We are using a constant amount of space to store the left, right, and mid pointers.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            sample = nums[mid]

            if sample == target:
                return mid
            elif sample < target:
                left = mid +1
            else:
                right = mid -1

        return -1