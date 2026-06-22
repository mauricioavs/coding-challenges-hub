# Complexity:
# Time: O(n): We traverse the list of temperatures once. While traversing, we may pop each index from the stack at most once, resulting in O(n) time complexity.
# Space: O(n): In the worst case, if the temperatures are in decreasing order, we will push all indices onto the stack, resulting in O(n) space complexity.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # saves indexes of pending temperatures

        for today, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                result[prev_day] = today - prev_day

            stack.append(today)

        return result