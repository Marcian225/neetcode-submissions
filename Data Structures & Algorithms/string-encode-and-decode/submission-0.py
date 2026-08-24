class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for word in strs:
            output += "#" + str(len(word))
            output += word

        return output


    def decode(self, s: str) -> List[str]:

        i = 0
        output = []
        while i < len(s):
            
            if s[i] == "#":
                nextword = ""
                i+= 1
                amount= int(s[i])
                for _ in range(amount):
                    i+=1
                    nextword += s[i]
                output.append(nextword)
                i+=1
        return output


