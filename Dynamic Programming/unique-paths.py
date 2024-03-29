class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r, c):
            
            if r > m or c>n : return 0
            if r == m and c == n: return 1
            if (r, c) not in memo: memo[(r, c)] = dp(r+1, c) + dp(r , c+1)
            return memo[(r, c)]
        return dp(1, 1)

        