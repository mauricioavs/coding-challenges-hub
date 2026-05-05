# Complexity:
# O(n^3) time: O(n^2) for loop and for each substring we check if it is a palindrome in O(n) time
# O(n) space: variable best and option take at most O(n) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = s[0]
        for i in range(len(s)):
            if len(best) >= len(s)-i:
                break
            for j in range(i+1, len(s)+1):
                # Iterate over all possible substrings and check if they are palindromes
                option = s[i:j]
                if len(best) >= len(option):
                    continue
                if self.isPalindrome(option):
                    best = option
        return best

    def isPalindrome(self, s: str) -> bool:
        # Iterate over the first half of the string and compare with the second half
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True
