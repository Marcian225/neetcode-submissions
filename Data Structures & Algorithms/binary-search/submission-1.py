class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binary_search(nums,target,0,len(nums)-1)

    def binary_search(self,nums,target,left,right) -> int:
        
        if not nums or left>right:
            return -1

        mid = left + (right-left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] <target:
            return self.binary_search(nums,target,mid+1,right)
        else:
            return self.binary_search(nums,target,0,mid-1)