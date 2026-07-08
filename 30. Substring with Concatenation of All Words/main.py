from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        sentence_len = len(words) * len(words[0])
        word_len = len(words[0])

        nums = []

        for p in range(len(s) - sentence_len + 1):
            sentence = s[p:p + sentence_len]

            found_words = []

            for k in range(0, sentence_len, word_len):
                word = sentence[k:k + word_len]
                found_words.append(word)

            if Counter(found_words) == Counter(words):
                nums.append(p)

        return nums
