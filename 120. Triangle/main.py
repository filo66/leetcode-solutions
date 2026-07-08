class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        memo = {}

        def solve(index:int , row:int):

            if (index,row) in memo:
                return memo[(index,row)]

            curent = triangle[row][index]

            if row == len(triangle) -1:
                return triangle[row][index]

            answer =  curent + min(solve(index+1 , row+1) , solve(index , row+1))

            memo[(index,row)] =answer
            return answer


        return solve(0,0)
