class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx , dy , x , y = 0,1,0,0

        for i in 4*instructions:
            if i =="G":
                x += dx
                y += dy
            elif i == "L":
                dx,dy = -dy ,dx
            else:
                dx,dy = dy , -dx

        return True if x == 0 and y == 0 else False
