class Solution:
    def minTriangleSum(self, triangle):
        n = len(triangle)
        m = n-1
        dp = [[-1]* i for i in range(1,n+1)]
        def helper(i,j):
            if j > i or j < 0:
                return int(1e9)
            if i == 0 :
                dp[0][j] = triangle[0][j]
                return triangle[0][j]
            if dp[i][j] != -1:
                return dp[i][j]
            up = triangle[i][j] + helper(i-1, j)
            up_left = triangle[i][j] + helper(i-1, j-1)
            dp[i][j]= min(up, up_left)
            return dp[i][j]
        
        min_ = float('inf')

        for j in range(n):
            ans = helper(n-1,j)
            min_ = min(min_, ans)
        return min_
