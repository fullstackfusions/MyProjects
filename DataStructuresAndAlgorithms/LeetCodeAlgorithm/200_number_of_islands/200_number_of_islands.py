'''
Time complexity : O(M \times N)O(MxN) where MM is the number of rows and NN is the number of columns.

Space complexity : worst case O(M \times N)O(MxN) in case that the grid map is filled with lands where DFS goes by M \times NMxN deep
'''
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid, row, col):
        #base case, if not 1, then its not an island
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != '1':
            return
        #update grid with islands we have visited already to not recount
        grid[row][col] = '#'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)

        