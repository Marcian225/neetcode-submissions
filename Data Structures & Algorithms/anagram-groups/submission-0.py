from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupsdict = defaultdict(list)
        n = len(strs)

        for word in strs:
            charssorted= sorted(word)
            word_sorted = "".join(charssorted)
            groupsdict[word_sorted].append(word)

        output = []
        for group in groupsdict.keys():
            output.append(groupsdict[group])
        return output



    # def isAnagram(self, s: str, t: str) -> bool:
    
    # if len(s) != len(t):
    #     return False

    # scharset = defaultdict(int)
    # for char in s:
    #     scharset[char] += 1


    # tcharset = defaultdict(int)
    # for x in t:
    #     tcharset[x] += 1


    # if scharset == tcharset:
    #     return True
    # else:
    #     return False