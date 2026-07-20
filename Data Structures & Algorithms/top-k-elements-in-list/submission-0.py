from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for number in nums:
            frequency[number] += 1

        sortedfreq = sorted(frequency.items(),key = lambda item: item[1], reverse = True)


        output = []
        i = 0
        for number in sortedfreq:

            if i == k: return output
            else:
                output.append(number[0])
            i+=1
        return output