'''
All numbers from 0 to n should exist

If one is not present in nums, that is the answer

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)+1):
            if i not in nums:
                return i

            
