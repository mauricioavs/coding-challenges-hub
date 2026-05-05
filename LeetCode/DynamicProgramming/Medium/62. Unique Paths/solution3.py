# Complexity:
# Time O(m+n): Each factorial is called at most m+n-2 times, and each call takes O(1) time due to memoization.
# Space O(m+n): The memory array stores the results of factorial calculations up to m+n-2.
# The problem of this method is that it can lead to integer overflow for large values of m and n, since factorial values grow very rapidly.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = [0] * (m+n-1)
        def factorial(n: int) -> int:
            if memory[n] != 0:
                return memory[n]
            if n == 0 or n == 1:
                return 1
            memory[n] = n * factorial(n-1)
            return memory[n]
        
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))