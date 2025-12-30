'''

Create an empty structure to remember seen numbers

Traverse the list value by value

For each number:

If it is already seen → duplicate → return True

Else → mark it as seen

If loop finishes → no duplicate → return False


'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new ={}
        
        for i in nums:
            if (i not in new):
                new[i] =i
               
            else:
                return True
        return False


           
        
