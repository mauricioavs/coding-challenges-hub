# Complexity:
# Time: O(n*m*k): where n is the length of the string, m is the number of words in the dictionary and k is the average length of the words in the dictionary.
# Space: O(n): where n is the length of the string.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        currIndex = 0
        n = len(s)
        mem = {}
        def solve():
            nonlocal currIndex

            if currIndex in mem:
                return False

            if currIndex==n:
                return True

            start = currIndex
            for word in wordDict:
                if s.startswith(word, currIndex):
                    currIndex+=len(word)
                    if solve():
                        return True
                    currIndex-=len(word)

            mem[start] = False
            return False
        return solve()