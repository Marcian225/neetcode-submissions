class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        scharset = set()
        for char in s:
            scharset.add(char)

        for char in t:
            if char in scharset: continue
            else: return False
        return True