class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #          x y
        current = [0,0]
        for i in moves:
            if i =="U":
                current[1] += 1
            elif i == "D":
                current[1] -= 1
            elif i == "R":
                current[0] += 1
            else :
                current[0] -= 1

        return True if current == [0,0] else False
