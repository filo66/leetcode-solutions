class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[1,2,3],
                [4,5,6],
                [9,8,7]]
        for i in range(len(moves)):
            if i % 2 == 0: # A
                grid[moves[i][0]][moves[i][1]] = "A"
            else: # B
                grid[moves[i][0]][moves[i][1]] = "B"

        if grid[0][0] == grid[0][1] == grid[0][2]:
            return grid[0][0]
        elif grid[1][0] == grid[1][1] == grid[1][2]:
            return grid[1][0]
        elif grid[2][0] == grid[2][1] == grid[2][2]:
            return grid[2][0]
        elif grid[0][0] == grid[1][0] == grid[2][0]:
            return grid[0][0]
        elif grid[0][1] == grid[1][1] == grid[2][1]:
            return grid[0][1]
        elif grid[0][2] == grid[1][2] == grid[2][2]:
            return grid[0][2]
        elif grid[0][0] == grid[1][1] == grid[2][2]:
            return grid[0][0]
        elif grid[0][2] == grid[1][1] == grid[2][0]:
            return grid[0][2]
        
        for i in grid:
            for j in i:
                try:
                    int(j)
                    return "Pending"
                except:
                    ...

        return "Draw"
