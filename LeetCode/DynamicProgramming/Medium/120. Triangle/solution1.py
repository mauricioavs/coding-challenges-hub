# Complexity:
# Time O(n^2): total of elements is 1 + 2 + ... + n = n * (n + 1) / 2, where n is the number of levels in the triangle.
# Space O(1): We modify the input triangle in place.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        levels = len(triangle)
    
        # Compute the leftmost and rightmost paths for each level, since they only have one path to follow.
        for lvl in range(1,levels):
            triangle[lvl][0] += triangle[lvl-1][0]
            triangle[lvl][-1] += triangle[lvl-1][-1]

        # Compute the minimum path for the inner elements of each level, since they have two paths to follow.
        for lvl in range(2,levels):
            for i in range(1, len(triangle[lvl])-1):
                triangle[lvl][i] += min(triangle[lvl-1][i-1], triangle[lvl-1][i])

        return min(triangle[-1])
