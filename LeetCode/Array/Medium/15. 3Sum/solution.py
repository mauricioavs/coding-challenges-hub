# Complexity:
# Time: O(n^2), where n is the number of elements in the input list. The outer loop runs O(n) times, and the inner while loop can also run O(n).
# Space: O(1) if we don't count the space used for the output list, since we are sorting the input list in place and using only a constant amount of extra space for pointers and temporary variables. The space used for the output list is O(k), where k is the number of unique triplets found.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for idx in range(len(nums) - 2):

            # Skip duplicate values for the first element of the triplet.
            # This prevents generating the same triplet multiple times.
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total < 0:
                    # Need a larger sum.
                    # Since the array is sorted, move left forward.
                    left += 1

                elif total > 0:
                    # Need a smaller sum.
                    # Since the array is sorted, move right backward.
                    right -= 1

                else:
                    result.append(
                        [nums[idx], nums[left], nums[right]]
                    )

                    # Move both pointers after finding a valid triplet.
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second element
                    # to avoid duplicate triplets.
                    while (
                        left < right and
                        nums[left] == nums[left - 1]
                    ):
                        left += 1

        return result