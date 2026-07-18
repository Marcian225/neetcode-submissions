class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsdict = set()
        for i in nums:
            if i in numsdict: return True
            else:
                numsdict.add(i)
        return False