class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {']':'[','}':'{', ')': '('}
        opening_brackets = []

        for char in s:
            if char in matching_brackets.values():
                opening_brackets.append(char)

            elif char in matching_brackets.keys():
                if not opening_brackets:
                    return False
                else:
                    if opening_brackets.pop() != matching_brackets[char]:
                        return False
        return len(opening_brackets) == 0