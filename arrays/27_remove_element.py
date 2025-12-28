"""
LeetCode 27 – Remove Element

Approach:
- Use a pointer `pos` to track the index for valid elements
- Copy elements that are not equal to `val` to the front
- Return the count of valid elements


"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos =0
        for i in range(len(nums)):
            if(nums[i]!= val):
                nums[pos] = nums[i]
                pos =pos+1
        return pos

       
