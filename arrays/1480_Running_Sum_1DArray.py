'''
The next value in running sum will be the sum of the previous value and the current value 
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        current = 0

        for num in nums:
            current += num
            runningSum.append(current)

        return runningSum
