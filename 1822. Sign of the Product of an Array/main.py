import math

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = math.prod(nums)

        if product <0:
            return -1
        elif product > 0:
            return 1
        else:
            return 0
