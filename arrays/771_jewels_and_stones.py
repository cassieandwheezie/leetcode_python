'''
i and j are characters not integers or indexex
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            for j in stones:
                if(i==j):
                    count+=1
        return count

        
