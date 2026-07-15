class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_lst = list(map(str , s))
        t_lst = list(map(str , t))

        for i in t_lst:
            if i in s_lst:
                s_lst.remove(i)
            else:
                return i
