'''







'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos=1
        for i in range(1,len(nums)):
            if(nums[pos-1]!=nums[i]):
                nums[pos] = nums[i]
                pos =pos+1
        return pos        
