class Solution:
    def ranking(self, text: str, num_row: int) -> list:
        text_len = len(text)
        try:
            num_of_repeats = 1 + (text_len - num_row + (num_row - 2)) // (num_row - 1)
            if num_of_repeats == 1 or num_of_repeats == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            return text

        row_orde = []
        for num in range(1, num_row + 1):
            row_orde.append(num)

        rank_lst = []

        for i in range(1, num_of_repeats + 1):
            if i == 1:
                rank_lst.extend(map(int, row_orde))
            else:
                if i % 2 == 1:  # It is odd.
                    compy_lst = list(map(int, row_orde))
                    compy_lst.pop(0)
                    rank_lst.extend(map(int, compy_lst))
                else:  # It is even.
                    compy_lst = list(map(lambda x: x, row_orde))
                    compy_lst.reverse()
                    compy_lst.pop(0)
                    rank_lst.extend(map(int, compy_lst))

        return rank_lst[:text_len]

    def convert(self, s: str, numRows: int) -> str:
        lsts = [[] for _ in range(numRows)]
        rank = self.ranking(s, numRows)

        if rank == s:
            return s

        for i, num in enumerate(rank):
            lsts[num - 1].append(s[i])

        txt = ""
        for i in lsts:
            txt += "".join(i)

        return txt
