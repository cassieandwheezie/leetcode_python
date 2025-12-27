"""
LeetCode 283 – Move Zeroes

Approach:
- Move non-zero elements forward
- Fill remaining positions with zero
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0 #initializing a pointer pos to have a check where I have to put non-zero items
        for i in range(len(nums)):
            if nums[i]!=0: #if the elemment is nn zero then move it forward 
                nums[pos]=nums[i]
                pos =pos+1

        for i in range(pos, len(nums)): #once all the non-zero elemnts are moved forward overwrite the rest of the elements as zero
            nums[i]=0

        

     

        
               
