class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(0,100):
            if pow(4,i)==n:
                return True
        return False
                
