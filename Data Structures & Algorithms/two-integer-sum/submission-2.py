class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rest = {}

        for index,value in enumerate(nums):
            comp = target - value
            if comp in rest:
                return [rest[comp],index]
            rest[value] = index

                        
