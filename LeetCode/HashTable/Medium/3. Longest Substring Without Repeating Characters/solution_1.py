class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_indices = {}
        left_idx = 0
        right_idx = 0
        longest_count = 0
        for i, char in enumerate(s):
            if char in letter_indices and letter_indices[char] >= left_idx:
                left_idx = letter_indices[char] + 1
            right_idx+=1
            letter_indices[char] = i
            longest_count = max(longest_count, right_idx-left_idx)
        return longest_count