# Complexity:
# Time O(min(m, n)): The loop runs min(m-1, n-1) times, which is the smaller of the two dimensions.
# Space O(1): We only use a constant amount of extra space.
# Combinatorics formula is: C(n, k) = n! / (k! * (n-k)!)
# Also it can be written asi C(n, k) = (n-k+1)(n-k+2)...n / 1*2*...*k
# This method is better than solution3 because it avoids the risk of integer overflow by calculating the result iteratively and using integer division at each step, which keeps the intermediate results manageable even for larger values of m and n.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        k = min(m - 1, n - 1)

        result = 1
        for i in range(1, k + 1):
            # How we know that result * (total - k + i) // i is always an integer?
            # i = 1: result = 1 * (total - k + 1) / 1 = (total-k+1)! / (total-k)!(1)! = C(total-k+1, 1) is an integer
            # i = 2: result = C(total-k+1, 1) * (total - k + 2) / (2) =  (total-k+1)! / (total-k)!(1)! * (total - k + 2) / (2) = (total-k+2)! / (total-k)!(2)! = C(total-k+2, 2) is an integer
            # i = 3: result = C(total-k+2, 2) * (total - k + 3) / (3) = (total-k+2)! / (total-k)!(2)! * (total - k + 3) / (3) = (total-k+3)! / (total-k)!(3)! = C(total-k+3, 3) is an integer
            # ...
            # I = k: result = C(total-k+k, k) = C(total, k) is an integer
            result = result * (total - k + i) // i

        return result