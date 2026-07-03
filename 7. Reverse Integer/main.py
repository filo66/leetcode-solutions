class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        num_lst = list(map(str , x))
        is_negative = None
        num_lst.reverse()
        if "-" in num_lst:
            is_negative = True
            num_lst.remove("-")
            new_num = ["-"]
            new_num.extend(num_lst)
            num = int("".join(new_num))
            return num if -2**31 <= num < 2**31 else 0
        else:
            num = int("".join(num_lst))
            return num if -2**31 <= num < 2**31 else 0
