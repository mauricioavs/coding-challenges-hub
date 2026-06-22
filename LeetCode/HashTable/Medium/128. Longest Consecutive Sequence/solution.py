# Complexity:
# Time: O(n), where n is the number of elements in the input list. We iterate through the list once to create the set and once to find the longest consecutive sequence.
# Space: O(n), since we store all the unique numbers in a set.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num -1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                best = max(best, length)

        return best