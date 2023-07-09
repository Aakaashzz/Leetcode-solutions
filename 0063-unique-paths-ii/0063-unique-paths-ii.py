class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1 - obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==0:
                    if j+1<n and obstacleGrid[i][j+1]!=1:
                        dp[i][j+1]+=dp[i][j]
                    if i+1<m and obstacleGrid[i+1][j]!=1:
                        dp[i+1][j]+=dp[i][j]
        
        return dp[m-1][n-1]