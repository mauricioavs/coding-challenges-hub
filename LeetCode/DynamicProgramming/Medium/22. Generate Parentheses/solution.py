# Complexity:
# O(C_n * n) time, where C_n is the nth Catalan number. This is because we generate C_n valid combinations of parentheses, and each combination takes O(n) time to construct.
# O(C_n * n) space, where C_n is the nth Catalan number. This is because we store C_n valid combinations of parentheses, and each combination takes O(n) space to store.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        par = []
        def dfs(open, closed):
            if open == closed == n:
                ans.append(''.join(par))
                return
            
            if open < n:
                par.append('(')
                dfs(open + 1, closed)
                par.pop()
            
            if open > closed:
                par.append(')')
                dfs(open, closed + 1)
                par.pop()
        
        dfs(0,0)
        return ans