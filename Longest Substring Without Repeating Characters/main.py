class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        avilable_text = []
        char_lst = []

        for i ,item in enumerate(s):
                try:
                    if s[i] not in char_lst:
                        char_lst.append(item)
                    else:
                        avilable_text.append("".join(char_lst))
                        while char_lst[0] != s[i]:
                            char_lst.pop(0)
                        char_lst.pop(0)
                        char_lst.append(s[i])
                except Exception as e:
                    print(e)
        avilable_text.append("".join(char_lst))

        for i , item in enumerate(avilable_text):
            avilable_text[i] = len(item)

        return max(avilable_text)
