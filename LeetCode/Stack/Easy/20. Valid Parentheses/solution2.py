# Complexity:
# Time: O(n): where n is the length of the input string s. We traverse the string once, and each character is processed in constant time.
# Space: O(n): in the worst case, if all characters in the string are opening parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
                continue
            if len(stack) == 0 or abs(ord(char) - ord(stack[-1])) > 2: # ord(')') - ord('(') = 1, ord(']') - ord('[') = 2, ord('}') - ord('{') = 2
                return False
            stack.pop()
        return len(stack) == 0
