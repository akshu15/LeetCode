class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
                return
            
            grid[i][j]='0'
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        row = len(grid)
        col = len(grid[0])
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count