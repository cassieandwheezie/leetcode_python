'''
for division remeber to use // instead of /
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums)//2
        low = 0
        high = len(nums) - 1
        while low <= high:
            if target > nums[middle]:
                low = middle+1
                middle = (low+high)//2
            elif target == nums[middle]:
                return middle
            else:
                high = middle-1
                middle = (low+high)//2

        return -1

            
