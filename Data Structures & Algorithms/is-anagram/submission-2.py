from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        scharset = defaultdict(int)
        for char in s:
            scharset[char] += 1


        tcharset = defaultdict(int)
        for x in t:
            tcharset[x] += 1


        if scharset == tcharset:
            return True
        else:
            return False
