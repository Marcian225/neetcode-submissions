class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, number in enumerate(nums):
            rest = target - number


            if rest in seen:
                return [seen[rest], index]

            seen[number] = index
