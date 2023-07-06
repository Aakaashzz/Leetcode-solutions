class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0]*n
        dp[-1]=1
        for i in range(n-2,-1,-1):
            for j in range(i,min(n,i+nums[i]+1)):
                if dp[j]==1:
                    dp[i]=1
                    break
        return dp[0]==1  