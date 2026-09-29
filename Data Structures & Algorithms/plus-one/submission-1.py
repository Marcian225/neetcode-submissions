class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1
        for i in range(last,-1,-1):
            if digits[i] == 9:
                if i == 0:
                    newlist = [0] * (len(digits)+1)
                    newlist[0] =1
                    return newlist
                else:
                    digits[i]=0
            else:
                digits[i]+=1
                return digits

                