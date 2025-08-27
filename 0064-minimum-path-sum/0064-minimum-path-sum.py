class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[0][0]=grid[0][0]
                    continue
                else:
                    up=dp[i][j-1]+grid[i][j] if j>0 else float('inf')
                    left=dp[i-1][j]+grid[i][j] if i>0 else float('inf')
                dp[i][j]=min(up,left)
        return dp[n-1][m-1]
