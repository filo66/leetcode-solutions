class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        try:
            dictionary = {}

            for i in strs:
                for j in range(len(i)+1) :
                    if i[0:j] not in dictionary.keys():
                        dictionary[i[0:j]] = 1
                    else:
                        dictionary[i[0:j]] += 1
            
            for key , value in list(dictionary.items()):
                if value != len(strs):
                    dictionary.pop(key)

            sorted_dict = dict(sorted(dictionary.items() , key=lambda item:len(item[0]) , reverse=True))
            return list(sorted_dict.keys())[0]
        except:
            return strs[0]
