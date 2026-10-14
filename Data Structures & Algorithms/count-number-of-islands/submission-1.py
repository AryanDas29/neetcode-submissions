class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 1 and 0 are actually strings 

        rows, cols = len(grid), len(grid[0])
        islands = 0 
        visited = set()

        # helper function 
        def dfs(r, c):
            # base cases 
            
            # out of bounds 
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            # water or already visited
            if (r, c) in visited or grid[r][c] == "0":
                return  
            
            visited.add((r, c))
            
            # recursively run dfs on all four directions

            dfs(r+1, c) # east
            dfs(r, c+1) # north 
            dfs(r-1, c) # west
            dfs(r, c-1) # south

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                dfs(r, c)

        return islands
            

            
            
