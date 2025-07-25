class Solution:
    def numTrees(self, n: int) -> int:
        def count_trees(start, end, memory: dict = {}) -> int:
            if start > end:
                return 1 # None
            if (start, end) in memory:
                return memory[(start, end)]

            total_count = 0
            for i in range(start, end+1):
                left = count_trees(start, i-1, memory)
                right = count_trees(i+1, end, memory)
                total_count += left * right 
            memory[(start, end)] = total_count 
            return total_count
        return count_trees(1, n)
