# Complexity:
# Time: O(n): where n is the length of the input array.
# Space: O(z): With z the number of zeroes in the array, we are using O(z) space to store the zeroes indexes.
# Search the zeroes in the array, and split the array in subarrays without zeros. 
# For each subarray, if the product of all its elements is negative, then the number os negativs is odd,
# so we can divide the total product by the multiplication of the elements until the first negative, or by the multiplication of the elements after the last negative, to get a positive product.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        zero_indexes = []
        n = len(nums)
        best = -float("inf")

        for i in range(n):
            if nums[i] == 0:
                zero_indexes.append(i)

        if len(zero_indexes) > 0:
            best = 0  # if some zero, at least best result is 0

        zero_indexes.append(n) # used to traverse the last part of array

        end = -1
        for zero_index in zero_indexes:
            start = end + 1 # first iteration start is 0, then is first zero index
            end = zero_index # first iteration end is first zero index, then is second zero index

            if end-start == 0: # no elements, used in case total array is [0]
                continue
            elif end-start == 1: # just one element
                best = max(best, nums[start])
                continue

            mult_til_first_neg = 1
            mult_after_last_neg = 1
            total_mult = 1
            for i in range(start, end):
                num = nums[i]
                total_mult *= num

                if mult_til_first_neg > 0:
                    mult_til_first_neg *= num

                if num < 0:
                    mult_after_last_neg = 1

                mult_after_last_neg *= num

            if total_mult < 0: # negatives are odd
                best = max(best, total_mult//mult_til_first_neg, total_mult//mult_after_last_neg)
            else:
                best = max(best, total_mult)

        return best
