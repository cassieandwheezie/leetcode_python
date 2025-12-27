"""
LeetCode 1929 – Concatenation of Array

Approach:
- Create a new array by concatenating nums with itself
"""

# Python’s list concatenation allows solving this problem without writing loops, resulting in concise and clean code.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans
     
