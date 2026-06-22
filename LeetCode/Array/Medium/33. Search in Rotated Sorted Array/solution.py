# Complexity:
# Time: O(log n): We perform two binary searches, each taking O(log n) time, resulting in O(log n) overall time complexity.
# Space: O(1): We are using a constant amount of space to store the pointers for the binary search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = nums.index(min(nums))

        result = self.binary_search(nums[:min_idx], target)

        if result != -1:
            return result
        
        result = self.binary_search(nums[min_idx:], target)
        
        if result != -1:
            return min_idx + result
        
        return -1
    
    def binary_search(self, nums: List[int], target: int) -> int:
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