# Manacher's algorithm
# Complexity:
# O(n) time: While loop executes as most O(n) times in the entire algorithm inside the for loop´.
# O(n) space: t is O(n) space, p is O(n) space, other variables are O(1) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "^#" + "#".join(s) + "#$"
        p = [0] * len(t) # len(t) = 2n + 3, so O(n) space

        center = 0
        right = 0

        best_center = 0
        best_len = 0

        for i in range (1, len(t)-1):
            # mirror is the index of the character that is the mirror of i with respect to the current center [... mirror ... center ... i ... right ...]
            mirror = 2 * center - i
            
            # we know the longest palindrome around mirror, so we can use that information to initialize p[i], but we can't go beyond right (unexplored area),
            # so we take the minimum of p[mirror] and right - i
            if i < right:
                p[i] = min(p[mirror], right-i)
            
            # expand around center i as long as the characters on both sides are equal
            # This causes expanding the "right" variable up to len(t) times
            # This makes it O(n) in total
            while t[i-1-p[i]] == t[i+1+p[i]]:
                p[i] += 1
            
            # Extend right
            if i + p[i] > right:
                center = i
                right = i + p[i]
            
            # Update best palindrome
            if p[i] > best_len:
                best_center = i
                best_len = p[i]
        
        first_char = (best_center -best_len ) // 2
        last_char = first_char + best_len 
        return s[first_char : last_char]