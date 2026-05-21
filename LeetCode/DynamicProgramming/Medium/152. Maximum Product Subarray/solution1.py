# Complexity:
# Time: O(n): where n is the length of the input array.
# Space: O(1): we are using constant space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best, min_prod, max_prod = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            possibility_1 = num * max_prod 
            possibility_2 = num * min_prod
            max_prod = max(num, possibility_1, possibility_2)
            min_prod = min(num, possibility_1, possibility_2)
            best = max(best, max_prod)

        return best
