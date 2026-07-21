class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashed = set(nums)

        longest_streak = 0 

        for num in hashed:

            if (num-1) not in hashed:
                current_num = num
                current_streak =1

                while (current_num+1) in hashed:
                    current_streak +=1
                    current_num += 1
                longest_streak = max(longest_streak,current_streak)

        return longest_streak