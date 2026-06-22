# Complexity:
# Time: O(n): where n is the length of the input string s. We traverse the string once, and each character is processed in constant time.
# Space: O(n): in the worst case, if all characters in the string are opening
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return not stack

