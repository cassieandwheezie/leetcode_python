'''
First Method :
| this is the bitwise orr not logical 
Therefore, use or in python 

Second Method:
In this we can do this by just finding a single + or - sign across the list elements 
Remenber that the entered number is a string not an inteher is you cannot check like 
if i=='+' instead check if'+' in i

'''

#First Method 

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for i in operations:
            if(i=='--X' or i=='X--'):
                X-=1
            else:
                X+=1
        return X

#Second Method
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if '-' in i:
                x -= 1
            else:
                x += 1
        return x
