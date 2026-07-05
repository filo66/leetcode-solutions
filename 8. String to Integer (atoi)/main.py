class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = ""

        try :
            assert len(s) >=1
            if s[0] == "-" :
                s = s.removeprefix("-")
                num += "-"
            elif s[0] == "+":
                s = s.removeprefix("+")
        except:
            return 0

        for i in s:
            try:
                int(i)
                num += "".join(i)
            except:
                break
        try:
            num = int(num)
            if not -2**31 <= num < 2**31:
                return -2**31 if num<0 else (2**31)-1
            return int(num)
        except:
            return 0
