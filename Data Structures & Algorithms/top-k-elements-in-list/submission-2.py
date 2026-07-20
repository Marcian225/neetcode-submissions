from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for number in nums:
            frequency[number] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num,count in frequency.items():
            buckets[count].append(num)

        output = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != []:
                for num in buckets[i]:
                    output.append(num)
                    if len(output) == k:
                        return output
