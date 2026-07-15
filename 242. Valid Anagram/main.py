class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(map(str , s))
        t = list(map(str , t))

        s.sort()
        t.sort()

        if s != t:
            return False
        
        return True
