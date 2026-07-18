from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        scharset = defaultdict()
        for char in s:
            if char in scharset:
                scharset[char] += 1
            else:
                scharset[char] = 0

        tcharset = defaultdict()
        for x in t:
            if x in tcharset:
                tcharset[x] += 1
            else:
                tcharset[x] = 0

        if scharset == tcharset:
            return True
        else:
            return False
