class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n =len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i<=m or j<=m or grid[i][j]!="1":
                return 0
            else:
                grid[i][j]="0"
                return 1+dfs(i+1,j)+dfs(j+1,i)+dfs(i-1,j)+dfs(i,j-1)
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    max_area=max(dfs(i,j),max_area)
        return max_area

        