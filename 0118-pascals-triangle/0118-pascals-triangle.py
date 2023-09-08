class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp=[]
        for i in range(1,n+1):
            dp.append([0]*i)
        for i in range(0,n):
            for j in range(0,i+1):
                if(j==0 or j==i):
                    #For leading and trailing of the row the 1 should be appended....
                    dp[i][j]=1
                else:
                    #The previous values both are added together
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp