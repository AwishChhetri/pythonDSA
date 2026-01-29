
# Recursion + Memoization
class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[-1 for _ in range(W+1)] for _ in range(n+1) ]
        def helper(W, val, wt, n):
            if W == 0  or n == 0:
                return 0
                
            if dp[n][W] != -1:
                return dp[n][W]
            
            if wt[n-1] <= W:
                dp[n][W]=max(
                    val[n-1] + helper (W-wt[n-1], val,wt,n-1), helper (W,val,wt,n-1)
                )
                return dp[n][W]
            elif wt[n-1] > W:
                dp[n][W]=helper(W,val,wt,n-1)
                return dp[n][W]
            
        return helper(W,val,wt,n)
  