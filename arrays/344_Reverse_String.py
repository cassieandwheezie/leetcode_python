'''

Swap first & last
Move left forward
Move right backward
Stop when they meet


'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right = len(s)-1
        while(left<right):
            s[left], s[right] = s[right], s[left]
            left +=1
            right-=1
            
        
