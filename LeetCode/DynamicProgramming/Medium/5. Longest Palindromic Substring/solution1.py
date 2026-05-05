# Complexity:
# O(n^2) time: O(n) for loop and for each center we expand at most O(n/2) times
# O(n) space: variable best and option take at most O(n) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # First best palindrome is the first character  
        best = s[0]
        for i in range(1,len(s)):
            # Check for odd length palindromes with center at i
            option = self.getLongestPalindrome(s, i, i)
            if len(option) > len(best):
                best = option
            # Check for even length palindromes with center between i-1 and i
            option = self.getLongestPalindrome(s, i-1, i)
            if len(option) > len(best):
                best = option
        return best

    def getLongestPalindrome(self, s: str, start: int, end: int) -> str:
        # Expand around the center while the characters at start and end are the same and within bounds
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start-=1
            end+=1
        return s[start+1:end]
