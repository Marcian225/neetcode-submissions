class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        string = str(n)
        
        while string not in cache:
            cache.add(string)
            sumsq = 0
            for char in string:
                sumsq += pow(int(char),2)

            if sumsq == 1:
                return True
            else:
                string = str(sumsq)
        return False        