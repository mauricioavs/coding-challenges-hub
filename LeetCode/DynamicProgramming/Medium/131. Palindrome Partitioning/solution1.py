# Complexity:
# Time O(n * 2^n): where n is the length of the input string. We have 2^n possible solutions and we need O(n) time to build each solution.
# Space O(n^2): memory for the isPalindrome function stores the results for all the possible substrings, which are near n^2.
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        solution = []
        solutions = []
        mem = {}
        # checks if the substring s[i:j+1] is a palindrome with memory
        def isPalindrome(i, j):
            if (i,j) in mem:
                return mem[(i,j)]

            mid = i + ( j - i + 1) // 2

            for k in range(mid-i):
                if s[i+k] != s[j-k]:
                    mem[(i,j)] = False
                    return False
            mem[(i,j)] = True
            return True

        # generates all the possible solutions with backtracking
        def solve(i):
            if i == n:
                j = 0
                built_solution = []
                for k in solution:
                    built_solution.append(s[j:(k+1)])
                    j = k+1
                solutions.append(built_solution)

            for k in range(i, n):
                if isPalindrome(i, k):
                    solution.append(k)
                    solve(k+1)
                    solution.pop()
        
        solve(0)
        return solutions