'''
We have to been given an positive integer and we have to find the smallest multiple. So, basically it is 
the LCM of the two numbers.
If the number is odd then the the result will be the number itself*2
Ex- The number is 9 so the result is 18

In the even case the number is itself 
Ex- The number is 6 then the output is 6 itself .


'''

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2!=0:
            return n*2
        else:
            return n
        
