"""
LeetCode 1920 – Build Array from Permutation

Approach:
- For each index i, use nums[i] as an index
- Append nums[nums[i]] to the answer array

"""
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(len(nums)):
           
            ans.append(nums[nums[i]])
        return ans
