class Solution:
    def shiftGrid(self, grid: list, k: int) -> list:
        for i in range(k):
            copyied_grid = list(map(list,grid))
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if j < len(grid[i])-1:
                        grid[i][j+1] = copyied_grid[i][j]
                    elif j == len(grid[i])-1 and i != len(grid)-1:
                        grid[i+1][0] = copyied_grid[i][j]
                    else:
                        grid[0][0] = copyied_grid[i][j]
        return grid
