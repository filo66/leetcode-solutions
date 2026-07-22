class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        x =0
        y = -1
        sum = 0
        for i in mat:
            sum += i[x]
            sum += i[y] if len(i) + y != x else 0

            x +=1
            y -= 1

        return sum
