'''

return sorted(x*x for x in nums)
can be implemented by this one line also 

'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums
