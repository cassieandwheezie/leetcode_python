class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0,int(num**0.5)+1):
            if i*i == num:
                return True
        return False
        
