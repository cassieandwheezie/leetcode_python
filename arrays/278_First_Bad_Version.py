# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
This is the correct solution but exceeds the time lmit 
So, the best way to is to binary search 
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n 
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low



        
        
