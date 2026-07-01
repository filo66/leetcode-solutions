class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        try:
            assert 2<= len(nums) <= 10**4
            map(lambda x: -10**9<= x <=10**9 , nums)
            assert -10**9 <= target <= 10**9
        except :
            return
        for index1 , i in enumerate(nums):
            for index2,j in enumerate(nums):
                if i + j == target and index1 != index2:
                    return [index1 , index2]
        return

answer = Solution().twoSum([3,3] , 6)
print(answer)
