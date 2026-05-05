# Complexity:
# O(n log n) time: log n levels of recursion, each with O(n) time to compute the best sum crossing the midpoint
# O(log n) space: log n levels of recursion, each with O(1) space to compute the best sum crossing the midpoint
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            best_left = solve(left, mid)
            best_right = solve(mid + 1, right)

            curr = nums[mid]
            best_sum_left = curr

            #Expand from the middle to the left and find the best sum
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_sum_left = max (curr, best_sum_left)
            
            curr = nums[mid + 1]
            best_sum_right = curr

            # Expand from the middle to the right and find the best sum
            for i in range(mid + 2, right + 1):
                curr += nums[i]
                best_sum_right = max (curr, best_sum_right)

            # center sum is the best sum crossing the midpoint, which is the sum of the best sum on the left and the best sum on the right       
            best_sum_center = best_sum_left + best_sum_right

            return max(best_left, best_right, best_sum_center)
        return solve(0, len(nums) - 1)