class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        print(s)

        left = 0
        right = len(s)-1

        # while left<right:
        #     if s[left] != s[right]:
        #         return False
        #     left +=1
        #     right -=1
        # return True
        return s == s[::-1]