class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diffrence = arr[1]-arr[0]
        for i in range(1,len(arr)):
            if (arr[i]-arr[i-1]) != diffrence:
                return False
            
        return True
