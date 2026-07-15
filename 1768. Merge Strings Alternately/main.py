class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leni = [""] * len(word1+word2)

        for i in range(len(leni)):
            if i%2 == 0:
                try:
                    leni[i] += word1[0]
                    word1 = word1.removeprefix(word1[0])
                except IndexError:
                    leni.append(word2)
                    break
            elif i%2 == 1:
                try : 
                    leni[i] += word2[0]
                    word2 = word2.removeprefix(word2[0])
                except IndexError:
                    leni.append(word1)
                    break

        return "".join(leni)
