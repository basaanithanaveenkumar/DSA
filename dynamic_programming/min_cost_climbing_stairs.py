class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1]) 
        return dp[n]
        # n=len(cost)
        # cache={0:0,1:0}
        # def min_cost(i):
        #     if i in cache:
        #         return cache[i]
        #     else:
        #         cache[i]=min(min_cost(i-2)+cost[i-2],min_cost(i-1)+cost[i-1])
        #         return cache[i]
        # return min_cost(n)               