# Complexity:
# Time: O(n * k log k), where n is the number of strings in the input list and k is the maximum length of a string. Sorting each string takes O(k log k) time, and we do this for all n strings.
# Space: O(n * k), since in the worst case, all strings could be different and we would store all of them in the groups dictionary.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
