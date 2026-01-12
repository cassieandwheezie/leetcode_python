class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0,100):
            if i*i == num:
                return True
        return False
        
